rf results; mkdir results
for i in {1..500}
    do  
    randseed.py    
    alborz;                                           # creat a random structure in posout.acf
    convert.py;                                       # convert posout.acf to poscur.ascii
    rm -f posout.acf
    if [ $i -lt 10 ]; then 
        mkdir t000${i}
        mv poscur.ascii t000${i}    
        cp template/* t000${i}; 
        mv t000${i} results/
        cd results/t000${i}
    elif [ $i -lt 100 ]; then
        mkdir t00${i}
        mv poscur.ascii t00${i}    
        cp template/* t00${i}; 
        mv t00${i} results/
        cd results/t00${i}
    elif [ $i -lt 1000 ]; then
        mkdir t0${i}
        mv poscur.ascii t0${i}    
        cp template/* t0${i}; 
        mv t0${i} results/
        cd results/t0${i}
    else
        mkdir t${i}
        mv poscur.ascii t${i}    
        cp template/* t${i}; 
        mv t${i} results/
        cd results/t${i}
    fi  
    sbatch run 
    # ~/MH/MHM_over_files/MHMoF.x >& o1 &
    cd ../..
    done

