#!/bin/sh

module purge
module load openmpi

logfile=npb-run-mpi.log
tmpf=npb.tmp.$$

echo "Date: `date`" >> $logfile
echo "Host: `hostname`" >> $logfile
echo "" >> $logfile

cnt=0
cntf=0
cntp=0

# Data Traffic benchmark DT is new in the NPB suite
# (released as part of NPB3.x-MPI package).
# ---------------------------------------------------------------------------
# THIS BENCHMARK IS INTENTIONALLY SKIPPED AS IT NEEDS SPECIAL CONSIDERATIONS
# ---------------------------------------------------------------------------
#
# DT is written in C and same executable can run on any number of processors,
# provided this number is not less than the number of nodes in the communication
# graph.  DT benchmark takes one argument: BH, WH, or SH. This argument
# specifies the communication graph Black Hole, White Hole, or SHuffle
# respectively. The current release contains verification numbers for
# CLASSES S, W, A, and B only.  Classes C and D are defined, but verification
# numbers are not provided in this release.

# The following table summarizes the number of nodes in the communication
# graph based on CLASS and graph TYPE.
#
# CLASS  N_Source N_Nodes(BH,WH) N_Nodes(SH)
#  S      4        5              12
#  W      8        11             32
#  A      16       21             80
#  B      32       43             192
#  C      64       85             448
#  D      128      171            1024
#----------------------------------------------------------------------------

test_aps="bt cg ep ft is lu mg sp"
test_classes="S A C"

export NPB_TIMER_FLAG=1

bindir=/usr/bin
outdir=./logs-mpi

if [ ! -d $outdir ]; then
   mkdir -p $outdir
fi

SECONDS=0

for class in $test_classes
do
   for ap in $test_aps
   do
      pgm=$ap.$class.x
      pgmx=$MPI_BIN/$pgm
      case="$pgm"
      cnt=$((cnt + 1))
      if [ -e $pgmx ]; then
         time mpiexec --use-hwthread-cpus $pgmx>>$tmpf 2>&1
         if cat $tmpf | grep -iq "Successful"; then
            echo ">>> $case - successful" | tee -a $logfile
         else
            echo "*** $case - FAILED" | tee -a $logfile
            cntf=$((cntf + 1))
         fi
         outf=$outdir/${ap}.${class}.out
         cat $tmpf >> $outf
         rm $tmpf
      else
         echo "... $case - not present" | tee -a $logfile
         cntp=$((cntp + 1))
      fi
   done
done

module unload openmpi

echo "" >> $logfile
echo "Date: `date`" >> $logfile
echo "Total number of cases: $cnt" | tee -a $logfile
echo "Total number of FAILED cases: $cntf" | tee -a $logfile
echo "Total number of not present cases: $cntp" | tee -a $logfile
echo "" >> $logfile

duration=$SECONDS
echo "Script took $(($duration / 60)) minutes and $(($duration % 60)) seconds to complete"
echo ""


