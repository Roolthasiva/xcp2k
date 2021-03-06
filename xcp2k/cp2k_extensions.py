# -*- coding: utf-8 -*-

from cp2k import *
from cp2k import logger
from types import MethodType


def run(self):
    """Monkey patch to submit job through the queue.

    If this is called, then the calculator thinks a job should be run.
    If we are in the queue, we should run it, otherwise, a job should
    be submitted.

    """

    # if we are in the queue and jasp is called or if we want to use
    # mode='run' , we should just run the job. First, we consider how.
    
    #print(os.environ)
    if self.xcp2krc['mode'] == 'run':
        # probably running at cmd line, in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode
    elif 'NHOSTS' in os.environ:
        # we are in the queue. determine if we should run serial
        # or parallel
        #NPROCS = os.environ['NSLOTS ']
        # no question. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        #parcmd = 'mpirun -np %i %s' % (NPROCS, cp2kcmd)
        exitcode = os.system(cp2kcmd)
        return exitcode
    elif 'SLURM_JOB_NODELIST' in os.environ:
        # we are in the queue. determine if we should run serial
        # or parallel
        # NPROCS = int(os.environ['SLURM_NTASKS'])
        # no question. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode
    elif 'PBS_NODEFILE' in os.environ:
        # we are in the queue. determine if we should run serial
        # or parallel
        # NPROCS = int(os.environ['SLURM_NTASKS'])
        # no question. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode


    # if you get here, a job is getting submitted

    jobname = self.prefix

    if self.xcp2krc['env'].upper() == 'SLURM':
        cmdlist = ['sbatch']
        cmdlist += ['--wait']
        cmdlist += ['--job-name', '{0}'.format(jobname)]
        cmdlist += ['--nodes', '{0}'.format(self.xcp2krc['nodes'])]
        cmdlist += ['--time', '{0}'.format(self.xcp2krc['time'])]
        # cmdlist += ['--ntasks-per-node', '{0}'.format(self.cpu)]
    if self.xcp2krc['env'].upper() == 'SGE':
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
        cmdlist += ['-pe', 'openmpi', '{0}'.format(self.cpu)]
    if self.xcp2krc['env'].upper() == 'gridview':
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
        cmdlist += ['-l', 'nodes=1:ppn={0}'.format(self.cpu)]
        cmdlist += ['-q', 'low']
    
    logger.debug(cmdlist)
    logger.debug(self.xcp2krc['script'])

    try:
        p=Popen(cmdlist, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate(self.xcp2krc['script'])
        if out == '' or err != '':
            raise Exception('something went wrong in job queue :\n\n{0}'.format(err))
    except:
            raise Exception('\n\n something went wrong in job queue.\n\n')
    logger.debug(out)
    if self.xcp2krc['env'].upper() == 'SLURM':
        job_id = int(out.split()[3])
    elif self.xcp2krc['env'].upper() == 'SGE':
        job_id = int(out.split()[2])
    elif self.xcp2krc['env'].upper() == 'gridview':
        job_id = int(out.split('.')[0]) 
    logger.debug('jobs_id = ', job_id)
        

    if self.xcp2krc['env'].upper() == 'SLURM':
        output = Popen("sacct -j %i" %(job_id), shell = True,
               stdin = PIPE,
               stdout = PIPE,
               stderr = PIPE).communicate()
        if "COMPLETED" in output[0] and output[0].split()[15]==self.prefix:
            return 
    elif self.xcp2krc['env'].upper() == 'SGE':
        output = Popen("qstat -j %i" %(job_id), shell = True,
               stdin = PIPE,
               stdout = PIPE,
               stderr = PIPE).communicate()
        if "do not exist" in output[1]:
            return 
    elif self.xcp2krc['env'].upper() == 'gridview':
        output = Popen("qstat -R %i" %(job_id), shell = True,
               stdin = PIPE,
               stdout = PIPE,
               stderr = PIPE).communicate()
        if "Unknown" in output[1]:
            return 
    print('jobs failed')


CP2K.run = MethodType(run, None, CP2K)


def create_cell(self, CELL, atoms):
    """Creates the cell for a SUBSYS from an ASE Atoms object.

    Creates the cell unit vectors and replicates the periodic boundary
    conditions. Notice that this doesn't affect the PBCs used for
    electrostatics! (use create_poisson())

    args:
        subsys: pycp2k.parsedclasses._subsys1
            The SUBSYS for which the cell is created.
        atoms: ASE Atoms
            The ASE Atoms object from which the cell is extracted.
    """
    cell = atoms.get_cell()
    A = cell[0, :]
    B = cell[1, :]
    C = cell[2, :]
    CELL.A = A.tolist()
    CELL.B = B.tolist()
    CELL.C = C.tolist()

    pbc = atoms.get_pbc()
    periodicity = []
    if pbc[0]:
        periodicity.append("X")
    if pbc[1]:
        periodicity.append("Y")
    if pbc[2]:
        periodicity.append("Z")
    if len(periodicity) == 0:
        CELL.Periodic = "NONE"
    else:
        CELL.Periodic = "".join(periodicity)
    #
    if hasattr(atoms, 'symmetry'):
        CELL.Symmetry = atoms.symmetry

CP2K.create_cell = MethodType(create_cell, None, CP2K)


def create_coord(self, COORD, atoms, molnames=None, symbol = 'True'):
    """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.

    args:
        subsys: pycp2k.parsedclasses._subsys1
        The SUBSYS for which the coordinates are created.
        atoms: ASE Atoms
        Atoms from which the coordinates are extracted.
        molnames: list of strings
        The MOLNAME for each atom in correct order
    """
    atom_list = []
    for i_atom, atom in enumerate(atoms):
        if symbol:
            new_atom = [atom.symbol, atom.position[0], atom.position[1], atom.position[2]]
        else:
            new_atom = [atom.position[0], atom.position[1], atom.position[2]]
        if molnames is not None:
            new_atom.append(molnames[i_atom])
        atom_list.append(new_atom)
    COORD.Default_keyword = atom_list

CP2K.create_coord = MethodType(create_coord, None, CP2K)


def create_constraint(self, constraint, atoms, molnames=None):
    """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.

    args:
        subsys: pycp2k.parsedclasses._subsys1
        The SUBSYS for which the coordinates are created.
        atoms: ASE Atoms
        Atoms from which the coordinates are extracted.
        molnames: list of strings
        The MOLNAME for each atom in correct order
    """
    #write constraint
    from ase.constraints import FixAtoms, FixScaled
    
    sflags = np.zeros((len(self.atoms), 3), dtype=bool)
    sflags_all = []
    if self.atoms.constraints:
        for constr in self.atoms.constraints:
            if isinstance(constr, FixScaled):
                sflags[constr.a] = constr.mask
            elif isinstance(constr, FixAtoms):
                sflags_all = constr.index
    # this is the same like "kind" module
    for iatom, atom in enumerate(self.atoms):
        fixed = ''.join([a for a, b in zip('XYZ', sflags[iatom]) if b])
        if len(fixed) != 0:
            fixed_atoms = constraint.FIXED_ATOMS_add()
            fixed_atoms.Components_to_fix = fixed
            fixed_atoms.List = iatom + 1
        
    
    fixed_lists = ''.join('  ' + str(x + 1) for x in sflags_all)
    #print(sflags_all)
    if len(sflags_all) != 0:
        fixed_atoms = constraint.FIXED_ATOMS_add()
        fixed_atoms.List = fixed_lists

CP2K.create_constraint = MethodType(create_constraint, None, CP2K)


def create_poisson(self, poisson, atoms):
    """Creates the periodicity for a POISSON section and tries to guess a
    good solver.

    args:
        poisson: pycp2k.parsedclasses._poisson1
        The poisson section from DFT or MM for which the periodicity is
        created.
        atoms: ASE Atoms
        The atoms from which the periodicity is extracted.
    """
    # Define periodicity
    pbc = atoms.get_pbc()
    if sum(pbc) == 0:
        poisson.Periodic = "NONE"
    else:
        poisson.Periodic = pbc[0]*"X" + pbc[1]*"Y" + pbc[2]*"Z"

CP2K.create_poisson = MethodType(create_poisson, None, CP2K)

def write_input_file(self):
    """Creates an input file for CP2K executable from the object tree
    defined in CP2K_INPUT.
    """
    #self.old_input = self.new_input
    #print("write_input_file")
    
    
    self.pre_write_input_file()

    SUBSYS = self.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS
    CONSTRAINT = self.CP2K_INPUT.MOTION.CONSTRAINT
    
    # write atoms
    self.create_cell(SUBSYS.CELL, self.atoms)
    self.create_coord(SUBSYS.COORD, self.atoms)
    self.create_constraint(CONSTRAINT, self.atoms)
    
    # write Kind
    #kinds = dict([(s.Section_parameters, s) for s in SUBSYS.KIND_list])
    #print(kinds)
    #for elem in set(self.atoms.get_chemical_symbols()):
    #    if elem not in kinds.keys():
    #        KIND = SUBSYS.KIND_add(elem)  # Section_parameters can be provided as argument.
    #        KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    #        KIND.Potential = "GTH-PBE"

     
    input_contents = self.CP2K_INPUT._print_input(-1)

    # Write the file
    if len(self.prefix) > 0 and not os.path.exists(self.directory):
            os.makedirs(self.directory)  # cp2k expects dirs to exist
    with open(join(self.directory, 'cp2k.inp'), 'w') as input_file:
        input_file.write(input_contents)

CP2K.write_input_file = MethodType(write_input_file, None, CP2K)


def pre_write_input_file(self):
    """Creates an input file for CP2K executable from the object tree
    defined in CP2K_INPUT.
    """
    #self.old_input = self.new_input
    #print("write_input_file")
    GLOBAL = self.CP2K_INPUT.GLOBAL
    FORCE_EVAL = self.CP2K_INPUT.FORCE_EVAL_list[0]
    DFT = FORCE_EVAL.DFT
    SCF = DFT.SCF

    # project name
    GLOBAL.Project_name = self.prefix
    if GLOBAL.Run_type is None:
        GLOBAL.Run_type = self.params['global']['RUN_TYPE']
    #
    if not FORCE_EVAL.Method:
        FORCE_EVAL.Method = "Quickstep"
    # xc functional 
    #if self.params['xc']['XC'] is not None:
    #    DFT.XC.XC_FUNCTIONAL.Section_parameters = self.params['xc']['XC']
    # forces
    #calc_forces = ['ENERGY_FORCE', 'GEO_OPT', 'CELL_OPT', 'MD']
    #if GLOBAL.Run_type.upper() in calc_forces:
    #    self.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES.Section_parameters = "ON"
        # ***todo
        #self.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES.Filename = "forces"

    # basis_set
    #if not DFT.Basis_set_file_name:
    #    DFT.Basis_set_file_name = "BASIS_MOLOPT"
    #if not DFT.Potential_file_name:
    #   DFT.Potential_file_name = "POTENTIAL"
    

CP2K.pre_write_input_file = MethodType(pre_write_input_file, None, CP2K)

