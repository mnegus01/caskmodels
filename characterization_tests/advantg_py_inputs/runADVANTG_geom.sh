#!bin/bash/

# Script to take a geometry as an input (i.e. sh runADVANTG_geom.sh maze1 )
# and then submit runscripts to the queue for that geometry

# Set variable geom to input
geom=$1
# Set variables to input/geometry/output paths
inpath=$2
geompath=$3
outpath=$4

# Check that the input location exists for runscfipts (and if not, give an error)
if [ -d $inpath ]; then
    # Check that the output location exists (and if not, create it)
    if [ ! -d $outpath$geom ]; then
	echo "Creating output directory for this geometry: $outpath$geom"
	mkdir $outpath$geom
    fi
    
    # Change to output directory 
    echo "Changing locations to geometry output directory: $outpath$geom"
    cd $outpath$geom

    # Loop over shell scripts of the specified geometry
    for file in "$inpath$geom"_*.sh; do
	# Check that the input geometry actually exists
	if [ $file = "$inpath$geom_*.sh" ]; then
	    echo "ERROR: No runscripts exist for geometry $file."
	else
	    runname=${file##/*/}
	    runname=${runname%.sh}
	    if [ ! -d $outpath$geom$runname ]; then
		pwd
		echo "Creating output directory for this run: $outpath$geom/$runname"		
		mkdir $runname
	    fi
	    echo "Changing location to run output directory: $outpath$geom$runname" 
	    cd $runname

	    # Copy MCNP geometries to output directory
	    echo "Copying geometry file to output directory"
	    cp "$geompath$geom".i .

	    #Submit jobs to Savio
	    echo "Submitting $file to the queue."
	    sbatch $file
	    cd ..
	fi
    done
else
    echo "ERROR: The input file location does not seem to exist."
fi

