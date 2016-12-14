#!bin/bash/

# Script to take a geometry as an input (i.e. sh runADVANTG_geom.sh maze1 )
# and then submit runscripts to the queue for that geometry

# Set variable geom to input
geom=$1
# Set variable method to method type (CADIS/FWCADIS)
method=$2
# Set variables to input/geometry/output paths
inpath=$3
geompath=$4
outpath=$5
scratchpath=$6

startpath=$(pwd)

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
	    runpath=$outpath$geom/$runname
	    if [ ! -d $outpath$geom/$runname ]; then
		echo "Creating output directory for this run: $runpath"		
		mkdir $runpath
	    fi
	    echo "Changing location to run output directory: $runpath" 
	    cd $runpath

	    # Copy MCNP geometries to output directory
	    echo "Copying geometry file to output directory"
	    cp "$geompath$geom"*-"$method"* .

	    # Submit jobs to Savio
	    echo "Submitting $file to the queue."
	    sbatch $file
	    cd $outpath$geom
	fi
    done
else
    echo "ERROR: The input file location does not seem to exist."
fi

if [ -z $scratchpath ]; then
	# Copy run files to scratch (use a batch job, with dependency set)
	if [ ! -d $scratchpath$geom ]; then
		mkdir $scratchpath$geom
	fi

	cd $startpath

	sed s/geom/$geom/ cpscratch.sh | tee cpscratch_temp.sh
	sed -i s/gjob/${runname:0:5}/ cpscratch_temp.sh
	sbatch cpscratch_temp.sh $geom $outpath $scratchpath
	rm -f cpscratch_temp.sh
fi


