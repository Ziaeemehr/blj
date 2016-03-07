alborz ; cp posout.acf  posout001.acf;  cat posout001.acf > posout001.ascii
alborz ; cp posout.acf  posout002.acf;  cat posout002.acf > posout002.ascii
alborz ; cp posout.acf  posout003.acf;  cat posout003.acf > posout003.ascii
alborz ; cp posout.acf  posout004.acf;  cat posout004.acf > posout004.ascii
alborz ; cp posout.acf  posout005.acf;  cat posout005.acf > posout005.ascii
alborz ; cp posout.acf  posout006.acf;  cat posout006.acf > posout006.ascii
alborz ; cp posout.acf  posout007.acf;  cat posout007.acf > posout007.ascii
alborz ; cp posout.acf  posout008.acf;  cat posout008.acf > posout008.ascii
alborz ; cp posout.acf  posout009.acf;  cat posout009.acf > posout009.ascii
alborz ; cp posout.acf  posout010.acf;  cat posout010.acf > posout010.ascii
rm posout*.acf; rm -rf t2; mkdir t2; mv posout*.ascii t2/
