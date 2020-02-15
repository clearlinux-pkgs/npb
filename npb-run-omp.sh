#!/bin/sh

module purge

logfile=npb-run-omp.log
tmpf=npb.tmp.$$

echo "Date: `date`" >> $logfile
echo "Host: `hostname`" >> $logfile
echo "" >> $logfile

cnt=0
cntf=0
cntp=0

test_aps="bt cg ep ft is lu mg sp ua"
test_classes="S A C"

#test_threads="4 8 16"
test_threads=`grep -c ^processor /proc/cpuinfo`

export NPB_TIMER_FLAG=1

bindir=/usr/bin
outdir=./logs-omp

if [ ! -d $outdir ]; then
   mkdir -p $outdir
fi

SECONDS=0

for nt in $test_threads
do
   export export OMP_NUM_THREADS=$nt

   for class in $test_classes
   do
      for ap in $test_aps
      do
         pgm=$ap.$class.x
         pgmx=$bindir/$pgm
         case="$pgm nt=$nt"
         cnt=$((cnt + 1))
         if [ -e $pgmx ]; then
            time $pgmx>>$tmpf 2>&1
            if cat $tmpf | grep -iq "Successful"; then
               echo ">>> $case - successful" | tee -a $logfile
            else
               echo "*** $case - FAILED" | tee -a $logfile
               cntf=$((cntf + 1))
            fi
            outf=$outdir/${ap}.${class}.out.${nt}
            cat $tmpf >> $outf
            rm $tmpf
         else
            echo "... $case - not present" | tee -a $logfile
            cntp=$((cntp + 1))
         fi
      done
   done
done

echo "" >> $logfile
echo "Date: `date`" >> $logfile
echo "Total number of cases: $cnt" | tee -a $logfile
echo "Total number of FAILED cases: $cntf" | tee -a $logfile
echo "Total number of not present cases: $cntp" | tee -a $logfile
echo "" >> $logfile

duration=$SECONDS
echo "Script took $(($duration / 60)) minutes and $(($duration % 60)) seconds to complete"
echo ""


