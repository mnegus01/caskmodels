README (modified 12/06/2016 by Mitch Negus)

Submitting ADVANTG on Savio

These files are used to 
(1) generate python driver ADVANTG inputs
	-advinpGen.py
(2) generate BASH runscripts with job information (1 job per python input)
	-runscriptGen.py
(3) submission script to submit jobs to Savio
	-runADVANTG_geom.sh


Steps (1) and (2) are accomplished using the advinpGen.py script (the ADVANTG Input Generator)
	-USER MUST MODIFY:
		infilepath	path to python driver input templates 
				(should be different for triangular and product quadrature types; 
				infilepath must end in "/")
		outfilepath	path to output directory containing "pydriver" and "runscript" directories
				("pydriver" & "runscript" are user-created; outfilepath must end in "/")
		geomnames	list of names of geometries to be processed (e.g. beam, maze1, maze2, reactor)
		quads		list of ADVANTG quadrature types (e.g. qr, levelsym, glproduct)
		triquadOs	list of triangular quadrature orders; only used for tri. quadrature types 
		prodquadOs	list of product quadrature orders; only used for prod. quadrature types
		pnOs		list of P_N orders to be processed
		
		(see 2013 ADVANTG input manual, sec 5.7 for limits on quads,triquadOs,prodquadOs, and pnOs)

	-user has the option of only generating python driver outputs or runscripts
	(toggle ADVANTGrun/SLURMrun flags 1=on/0=off)
	
	-advinpGen.py calls runscriptGen.py; no further user action required

	-outputs take the form of python scripts with name "[geomname]_[quad]_[quadO]-[pnO].py" where each
	bracketed item corresponds to the respective element in the given lists defined by the user.

Step (3) is accomplished using the runADVANTG_geom.sh script
	-USER MUST PROVIDE OPTIONS UPON RUNNING
		1) geom		Geometry (e.g. beam, maze1, maze2, reactor)
		2) inpath	path to directory containing runscripts	
		3) geompath	path to directory containing geometries
		4) outpath	path to directory where outputs will be delivered (likely on scratch)
		
		ex: sh runADVANTG_geom.sh /path1/to/runscripts/ /path2/to/Geometries/ /path3/to/ADVANTG_outputs
		
	-Upon running, runADVANTG_geom.sh will create an output directory for all outputs for a given geometry if
	it doesn't already exist. Within this directory, the script will create sub-directories for each run 
	(unique to a python input and runscript). ADVANTG outputs for a run will be located in these directories. 

	-MCNP geometry for the run will be copied to the run sub-directory for access by ADVANTG.





Questions? Contact negus@berkeley.edu
