c==================================================================================c
c - Program for 3D anisotropic hardening                                           c
c - Anisotropic Hill48 yield function                                              c
c - Hill7 - anisotropic hardening & r-value evolution                              c
c - Junhe Lian                                                                     c
c - junhe.lian@iehk.rwth-aachen.de                                                 c
c==================================================================================c
c - Coupled with the Modified Bai Wierzbicki (MBW) damage model                    c
c - Fuhui Shen                                                                     c
c - Integrity of Materials and Structures                                          c
c - Institut fuer Eisenhuettenkunde/Steel Institute (IEHK)                         c
c - RWTH Aachen University                                                         c
c - Intzestrasse 1                                                                 c
c - 52072 Aachen                                                                   c
c - Germany                                                                        c
c - Fuhui.Shen@iehk.rwth-aachen.de                                                 c
c----------------------------------------------------------------------------------c
c - Damage initiation according to 3D fracture locus (equivalent plastic strain to c
c   failure initiation being function of both hydrostatic pressure and lode angle) c
c - Damage evolution based on energy dissipated during damage process              c
c - Temperature softening                                                          c
c - Strain rate hardening                                                          c
c - Non-proportional Loading paths with varying stress states are considered with  c
c   weighting scheme for both                                                      c
c   cleavage fracture and ductile damage                                           c
c - Cut-off value concept is considered                                            c
c----------------------------------------------------------------------------------c
c Solution dependent variables (SDVs):                                             c
c SDV1:  Equivalent plastic strain                                                 c
c SDV2:  Equivalent stress                                                         c
c SDV3:  Temperature                                                               c
c SDV4:  Temperature softening factor                                              c
c SDV5:  Strain rate                                                               c
c SDV6:  Strain rate multipler factor                                              c
c SDV7:  Strain rate addition factor                                               c
c SDV8:  Strain rate: accumulation number                                          c
c SDV9:  Strain rate: strain accumulation                                          c
c SDV10: Strain rate: time accumulation                                            c
c SDV11: Strain rate: averaged strain increment                                    c
c SDV12: Strain rate at real time step                                             c
c SDV13: Cleavage fracture indicator                                               c
c SDV14: Cleavage fracture stress criterion indicator                              c
c SDV15: Cleavage fracture strain criterion indicator                              c
c SDV16: Ductile damage initiation indicator                                       c
c SDV17: Ductile fracture indicator                                                c
c SDV18: Damage variable                                                           c
c SDV19: Von Mises equivalent stress                                               c
c SDV20: Stress triaxiality                                                        c
c SDV21: Lode angle                                                                c
c SDV22: Normalized Lode angle                                                     c
c SDV23: Cleavage fracture initiation strain                                       c
c SDV24: Ductile fracture initiation strain                                        c
c SDV25: Critical ductile damage variable                                          c
c SDV26: Maximal principal stress                                                  c
c SDV27: Ductile damage initiation stress                                          c
c SDV28: Ductile damage initiation strain                                          c
c SDV29: Element deletion flag                                                     c
c SDV30: Element deletion                                                          c
c==================================================================================c
c          !DO NOT DISTRIBUTE WITHOUT AUTHOR'S PERMISSION!                         c
c==================================================================================c
       subroutine vumat(
C Read only -
     1  nblock, ndir, nshr, nstatev, nfieldv, nprops, lanneal,
     2  stepTime, totalTime, dt, cmname, coordMp, charLength,
     3  props, density, strainInc, relSpinInc,
     4  tempOld, stretchOld, defgradOld, fieldOld,
     3  stressOld, stateOld, enerInternOld, enerInelasOld,
     6  tempNew, stretchNew, defgradNew, fieldNew,
C Write only -
     5  stressNew, stateNew, enerInternNew, enerInelasNew)
C
      include 'vaba_param.inc'
C
C All arrays dimensioned by (*) are not used in this algorithm
      dimension props(nprops), density(nblock),
     1  coordMp(nblock,*),
     2  charLength(*), strainInc(nblock,ndir+nshr),
     3  relSpinInc(*), tempOld(*),
     4  stretchOld(*), defgradOld(*),
     5  fieldOld(*), stressOld(nblock,ndir+nshr),
     6  stateOld(nblock,nstatev), enerInternOld(nblock),
     7  enerInelasOld(nblock), tempNew(*),
     8  stretchNew(*), defgradNew(*), fieldNew(*),
     9  stressNew(nblock,ndir+nshr), stateNew(nblock,nstatev),
     1  enerInternNew(nblock), enerInelasNew(nblock)
C
      character*80 cmname
C
C Defining numerical constants
      parameter(zero=0.,one=1.,two=2.,three=3.,four=4.,six=6.,
     1  half=0.5,threeHalves = 1.5,third = one/three,Tol=1.D-6,
     1  twoThirds=two/three,const1=sqrt(threeHalves),NTENS=6,NDI=3)
      REAL A0,e0,xn0,A45,e45,xn45,A90,e90,xn90,AEB,eEB,xnEB,r0,r45,r90,
     1  rEB,F,G,H,L,M,N,F1,G1,H1,L1,M1,N1,T0,cT1,cT2,cT3,Dens,Cp,Delta,
     1  StraRate0,cE1,cE2,cE3	 
C     User defined tensors
      DIMENSION dfds(6),Ydirection(6),dgds(6),DSTRESS(6),
     1 ST(6),EELAS(6),EPLAS(6),EELT(6),EPLT(6),STRESST(6),
     2 EELAST(6),EPLAST(6),DDSDDE(6,6),DSTRAN(6) 
C Define material properties constants
c ELASTIC properties
       EMOD = PROPS(1)
       ENU  = PROPS(2)
c ELASTIC STIFFNESS
       EBULK3=EMOD/(one-two*ENU)
       EG2=EMOD/(one+ENU)
       EG=EG2/two
       EG3=three*EG
       ELAM=(EBULK3-EG2)/three
       PI= four*atan(one)
c Define temperature and temperature softening parameters
       T0= PROPS(9)	  
       cT1 = PROPS(10)
       cT2 = PROPS(11)
       cT3 = PROPS(12)
       Dens = PROPS(13)
       Cp = PROPS(14)
       Delta = PROPS(15)
c Define strain rate and strain rate hardening parameters  
       StraRate0 = PROPS(17)	
       cE1 = PROPS(18)
       cE2 = PROPS(19)
       cE3 = PROPS(20) 
       Nrincr = PROPS(21)
c Define cleavage fracture stress
       Sigcf = PROPS(25) 
c Define cleavage fracture locus parameters	
       Cc1 = props(26)
       Cc2 = props(27)
       Cc3 = props(28)
       Cc4 = props(29)
c Define Cut-off value	  
       Cut = props(33)
c Define damage energy dissipation parameter 	  
       Gf = props(34)	   
c Define ductile damage initiation locus parameters	  
       Ddi1 = props(35)
       Ddi2 = props(36)
       Ddi3 = props(37)
       Ddi4 = props(38)
       Ddi5 = props(39)
       Ddi6 = props(40)
c Define ductile fracture locus parameters	  
       Dc1 = props(41)
       Dc2 = props(42)
       Dc3 = props(43)
       Dc4 = props(44)	   
c Define dimension of flow curve and r-value input table	   
       nvalue = (nprops-48)/8	   
C----------------------------------------------------------------------C
C Computation per material point starts here
      do 9000 i = 1,nblock
C Fill in the elastic stiffness tensor
      DO 20 K1=1,NTENS
        DO 10 K2=1,NTENS
          DDSDDE(K2,K1)=zero
 10     CONTINUE
 20   CONTINUE
C
      DO 40 K1=1,NDI
        DO 30 K2=1,NDI
          DDSDDE(K2,K1)=ELAM
 30     CONTINUE
        DDSDDE(K1,K1)=EG2+ELAM
 40   CONTINUE
      DO 50 K1=NDI+1,NTENS
        DDSDDE(K1,K1)=EG
 50   CONTINUE
C  Elastic predictor and plastic corrector scheme in conjuction with the
C  Tangent Cutting Plane (TCP) algorithm 
C  Elastic predictor
      eqplastrue = stateOld(i,1)
      eqplas = eqplastrue
      AAA = stateOld(i,13) 
      AAAA = stateOld(i,14) 
      AAAB = stateOld(i,15)
      BBBB = stateOld(i,16) 
      BBB = stateOld(i,17) 
      Damage = stateOld(i,18)
      if(BBBB.lt.one) then
         Damage = zero
      endif	
      facDctDamDev = one - Damage
      facDctDamVol = facDctDamDev
      Fracflag = stateOld(i,29)
      Deletion = one
      stateNew(i,30) = Deletion	  	  
C Transite DSTRAN from strainInc, note diff. between UMAT and VUMAT.  
      DSTRAN(1)=strainInc(i,1)
      DSTRAN(2)=strainInc(i,2)
      DSTRAN(3)=strainInc(i,3)
      DSTRAN(4)=strainInc(i,4)*two
      DSTRAN(5)=strainInc(i,5)*two
      DSTRAN(6)=strainInc(i,6)*two
C Calculate Trial stress
      DO 70 K1=1,NTENS
          STRESST(K1)=stressOld(i,K1)+(DDSDDE(K1,1)*DSTRAN(1)
     1   +DDSDDE(K1,2)*DSTRAN(2)+DDSDDE(K1,3)*DSTRAN(3)
     1   +DDSDDE(K1,4)*DSTRAN(4)+DDSDDE(K1,5)*DSTRAN(5)
     1   +DDSDDE(K1,6)*DSTRAN(6))*facDctDamDev
 70   CONTINUE
C If brittle fracture has previously occured, stress is zeroed
        if(Fracflag.gt.(three-half).and. Fracflag.lt.(three+half))then
           STRESST(1) = zero
           STRESST(2) = zero
           STRESST(3) = zero
           STRESST(4) = zero
           STRESST(5) = zero
           STRESST(6) = zero
           Fracflag = three
           AAA = one
           Deletion = zero
          goto 9000
        endif
C If ductile fracture has previously occured, stress is zeroed
        if(Fracflag.gt.(two-half) .and. Fracflag.lt.(two+half))then
           STRESST(1) = zero
           STRESST(2) = zero
           STRESST(3) = zero
           STRESST(4) = zero
           STRESST(5) = zero
           STRESST(6) = zero
           Fracflag = two
           BBB = one
           Deletion = zero
          goto 9000
        endif
       ST1=STRESST(1)
       ST2=STRESST(2)
       ST3=STRESST(3)
       ST4=STRESST(4)
       ST5=STRESST(5)
       ST6=STRESST(6)
C Calculating softening correction term due to temperature rise
       T=stateOld(i,3)
        if(T.le.Tol .and. T.ge.(zero-Tol)) then
          T=T0
        endif
        facT = cT1*exp(zero-cT2*T)+cT3
C Calculating hardening correction terms due to straining rate
       StraRate=stateOld(i,5)
        if(StraRate.le.Tol .and. StraRate.ge.(zero-Tol)) then
          StraRate=StraRate0
        endif
       facStraRateM = cE1*log(StraRate) + cE2
       facStraRateA = cE3*StraRate
C Preventing negative values for straining rate
       if(facStraRateM.lt.one) facStraRateM = one		   
C Calculate anisotropic parameters in Hill48 based on flow stresses	          
C Fetching yield stress from flow curve
       call ahard(sigmayield0,hard0,sigmayield45,sigmayield90,
     1   sigmayieldEB,rvalue0,rvalue45,rvalue90,eqplas,PROPS(49),
     1   nvalue)	   
       sigmayield=sigmayield0
       xhard=hard0
       s0=sigmayield
       s45=sigmayield45
       s90=sigmayield90
       sEB=sigmayieldEB
       F=((s0**2)/(s90**2)-one+(s0**2/sEB**2))/two
       G=(one-(s0**2/s90**2)+(s0**2/sEB**2))/two
       H=(one+(s0**2/s90**2)-(s0**2/sEB**2))/two
       N=((four*s0**2/s45**2)-(s0**2/sEB**2))/two
       L=threeHalves
       M=threeHalves
C Calculate subvalue of the trial Hill48 equivalent stress		   
       subsigtrial= F*(ST2-ST3)**2+G*(ST3-ST1)**2
     1             +H*(ST1-ST2)**2+two*N*ST4**2
     2             +two*L*ST5**2+two*M*ST6**2
c To prevent subsigtrial =0
       if(subsigtrial.lt.Tol) subsigtrial = Tol
C Calculate the trial Hill48 equivalent stress 
       sigtrial = sqrt(subsigtrial)
c To prevent sigtrial =0	   
       if(sigtrial.lt.Tol .and. sigtrial.ge.zero) sigtrial = Tol
       if(sigtrial.gt.(zero-Tol) .and. sigtrial.le.zero) then 
          sigtrial = zero-Tol	   
       endif	   
! Keep the yield stress
       Sigdi = stateOld(i,27)
       Epsdi = stateOld(i,28)
       stateNew(i,31) = stateOld(i,31)	 
C Check yielding
       radius=(sigmayield*facStraRateM+facStraRateA)*facT*facDctDamDev
       Xhardnew=(xhard)*facStraRateM*facT*facDctDamDev
       xf = sigtrial - radius
       if(xf.le.(Tol)) then            		 
          goto 1000
       endif
       dgama=zero
       iflag=zero 
C Plastic corrector and Begin iterations
5000   continue
       iflag=iflag+one   
c Calculate anisotropic parameters in Hill48 based on flow stresses
C Fetching yield stress from flow curve
       call ahard(sigmayield0,hard0,sigmayield45,sigmayield90,
     1   sigmayieldEB,rvalue0,rvalue45,rvalue90,eqplas,PROPS(49),
     1	 nvalue)	   
       sigmayield=sigmayield0
       xhard=hard0
       s0=sigmayield
       s45=sigmayield45
       s90=sigmayield90
       sEB=sigmayieldEB
       r0=rvalue0
       r45=rvalue45
       r90=rvalue90
       F=((s0**2)/(s90**2)-one+(s0**2/sEB**2))/two
       G=(one-(s0**2/s90**2)+(s0**2/sEB**2))/two
       H=(one+(s0**2/s90**2)-(s0**2/sEB**2))/two
       N=((four*s0**2/s45**2)-(s0**2/sEB**2))/two
       L=threeHalves
       M=threeHalves
C Calculate subvalue of the trial Hill48 equivalent stress		   
       subsigtrial=F*(ST2-ST3)**2+G*(ST3-ST1)**2
     1             +H*(ST1-ST2)**2+two*N*ST4**2
     2             +two*L*ST5**2+two*M*ST6**2
c To prevent subsigtrial =0	 
       if(subsigtrial.lt.Tol) subsigtrial = Tol
C Calculate the trial Hill48 equivalent stress	   
       sigtrial = sqrt(subsigtrial)
c To prevent sigtrial =0	   
       if(sigtrial.lt.Tol .and. sigtrial.ge.zero) sigtrial = Tol
       if(sigtrial.gt.(zero-Tol) .and. sigtrial.le.zero) then
          sigtrial = zero-Tol
       endif
c Calculate anisotropic parameters in Hill48 based on r-values	 
       F1=r0/(r90)/(one+r0)
       G1=one/(one+r0)
       H1=r0/(one+r0)
       L1=threeHalves
       M1=threeHalves
       N1=(r0+r90)*(one+two*r45)/two/r90/(one+r0)
C Calculate subvalue of the trial Hill48 flow potential
       subsigmaHill=F1*(ST2-ST3)**2+G1*(ST3-ST1)**2
     1          +H1*(ST1-ST2)**2+two*N1*ST4**2
     2          +two*L1*ST5**2+two*M1*ST6**2
c To prevent subsigmaHill =0	 
       if(subsigmaHill.lt.Tol) subsigmaHill = Tol
C Calculate the trial Hill48 flow potential	   
       sigmaHill=sqrt(subsigmaHill)
c To prevent sigmaHill =0	   
       if(sigmaHill.lt.Tol .and. sigmaHill.ge.zero) sigmaHill = Tol
       if(sigmaHill.gt.(zero-Tol) .and. sigmaHill.le.zero) then
          sigmaHill = zero-Tol
       endif		   
C Update parameters with Non-AFR and calculate sigmayield and sigmaHill at every iteration 
C Calculate the flow direction vector based on Flow potential
       dgds(1)=(H1*(ST1-ST2)-G1*(ST3-ST1))/sigmaHill
       dgds(2)=(F1*(ST2-ST3)-H1*(ST1-ST2))/sigmaHill
       dgds(3)=(G1*(ST3-ST1)-F1*(ST2-ST3))/sigmaHill    
       dgds(4)=(two*N1*ST4)/sigmaHill
       dgds(5)=(two*L1*ST5)/sigmaHill
       dgds(6)=(two*M1*ST6)/sigmaHill
C Calculate the flow direction vector based on Yield function 
       dfds(1)=(H*(ST1-ST2)-G*(ST3-ST1))/sigtrial
       dfds(2)=(F*(ST2-ST3)-H*(ST1-ST2))/sigtrial
       dfds(3)=(G*(ST3-ST1)-F*(ST2-ST3))/sigtrial 
       dfds(4)=(two*N*ST4)/sigtrial
       dfds(5)=(two*L*ST5)/sigtrial
       dfds(6)=(two*M*ST6)/sigtrial
C Calculate the flow direction in the TCP algorithm
       Ydirection(1)=(dgds(1)*DDSDDE(1,1)+dgds(2)*DDSDDE(1,2)
     1              +dgds(3)*DDSDDE(1,3)+dgds(4)*DDSDDE(1,4)
     1  +dgds(5)*DDSDDE(1,5)+dgds(6)*DDSDDE(1,6))*facDctDamDev
       Ydirection(2)=(dgds(1)*DDSDDE(2,1)+dgds(2)*DDSDDE(2,2)
     1              +dgds(3)*DDSDDE(2,3)+dgds(4)*DDSDDE(2,4)
     1  +dgds(5)*DDSDDE(2,5)+dgds(6)*DDSDDE(2,6))*facDctDamDev
       Ydirection(3)=(dgds(1)*DDSDDE(3,1)+dgds(2)*DDSDDE(3,2)
     1              +dgds(3)*DDSDDE(3,3)+dgds(4)*DDSDDE(3,4)
     1  +dgds(5)*DDSDDE(3,5)+dgds(6)*DDSDDE(3,6))*facDctDamDev
       Ydirection(4)=(dgds(1)*DDSDDE(4,1)+dgds(2)*DDSDDE(4,2)
     1              +dgds(3)*DDSDDE(4,3)+dgds(4)*DDSDDE(4,4)
     1  +dgds(5)*DDSDDE(4,5)+dgds(6)*DDSDDE(4,6))*facDctDamDev
       Ydirection(5)=(dgds(1)*DDSDDE(5,1)+dgds(2)*DDSDDE(5,2)
     1              +dgds(3)*DDSDDE(5,3)+dgds(4)*DDSDDE(5,4)
     1  +dgds(5)*DDSDDE(5,5)+dgds(6)*DDSDDE(5,6))*facDctDamDev
       Ydirection(6)=(dgds(1)*DDSDDE(6,1)+dgds(2)*DDSDDE(6,2)
     1              +dgds(3)*DDSDDE(6,3)+dgds(4)*DDSDDE(6,4)
     1  +dgds(5)*DDSDDE(6,5)+dgds(6)*DDSDDE(6,6))*facDctDamDev
C Calculate the first term in the TCP algorithm
c dsdgama caculation=CNN, dot product, prepare for iteration
C Calculate MCN
       dsdga=dfds(1)*Ydirection(1)+dfds(2)*Ydirection(2)
     1      +dfds(3)*Ydirection(3)+dfds(4)*Ydirection(4)
     1      +dfds(5)*Ydirection(5)+dfds(6)*Ydirection(6)
C Calculate the second term in the TCP algorithm
C Correspongding flow direction, Nf
       radius=(sigmayield*facStraRateM+facStraRateA)*facT*facDctDamDev
       Xhardnew=(xhard)*facStraRateM*facT*facDctDamDev
       Xdeltagamma = dsdga+Xhardnew	   
c To prevent Xdeltagamma =0	   
       if(Xdeltagamma.lt.Tol .and. Xdeltagamma.ge.zero) Xdeltagamma=Tol
       if(Xdeltagamma.gt.(zero-Tol) .and. Xdeltagamma.le.zero) then
          Xdeltagamma=zero-Tol
       endif   
       xddgamma = xf/Xdeltagamma
       dgama = dgama+xddgamma
c Update trial stress with new dgama
      STRESST(1)=stressOld(i,1)+(DDSDDE(1,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(1,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(1,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(1,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(1,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(1,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(2)=stressOld(i,2)+(DDSDDE(2,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(2,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(2,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(2,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(2,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(2,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev	  
      STRESST(3)=stressOld(i,3)+(DDSDDE(3,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(3,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(3,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(3,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(3,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(3,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(4)=stressOld(i,4)+(DDSDDE(4,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(4,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(4,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(4,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(4,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(4,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(5)=stressOld(i,5)+(DDSDDE(5,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(5,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(5,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(5,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(5,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(5,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(6)=stressOld(i,6)+(DDSDDE(6,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(6,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(6,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(6,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(6,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(6,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
c Update stress tensors
      ST1=STRESST(1)
      ST2=STRESST(2)
      ST3=STRESST(3)
      ST4=STRESST(4)
      ST5=STRESST(5)
      ST6=STRESST(6)
      StressTrace = ST1 + ST2 + ST3
C Update the equivalent plastic strain	  
      eqplastrue = stateOld(i,1)
      eqplas = eqplastrue+dgama*(sigmaHill/sigtrial)
      deqplas = dgama*(sigmaHill/sigtrial)	  
C Update anisotropic parameters in Hill48 based on flow stresses
C Fetching yield stress from flow curve
       call ahard(sigmayield0,hard0,sigmayield45,sigmayield90,
     1	 sigmayieldEB,rvalue0,rvalue45,rvalue90,eqplas,PROPS(49),
     1	 nvalue)	   
       sigmayield=sigmayield0
       xhard=hard0
       radius=(sigmayield*facStraRateM+facStraRateA)*facT*facDctDamDev   
       s0=sigmayield
       s45=sigmayield45
       s90=sigmayield90
       sEB=sigmayieldEB
       F=((s0**2)/(s90**2)-one+(s0**2/sEB**2))/two
       G=(one-(s0**2/s90**2)+(s0**2/sEB**2))/two
       H=(one+(s0**2/s90**2)-(s0**2/sEB**2))/two
       N=((four*s0**2/s45**2)-(s0**2/sEB**2))/two
       L=threeHalves
       M=threeHalves
C Update subvalue of the trial Hill48 equivalent stress	   
       subsigtrial=F*(ST2-ST3)**2+G*(ST3-ST1)**2
     1            +H*(ST1-ST2)**2+two*N*ST4**2
     2            +two*L*ST5**2+two*M*ST6**2
c To prevent subsigtrial =0	 
       if(subsigtrial.lt.Tol) subsigtrial = Tol
C Update the trial Hill48 equivalent stress 	   
       sigtrial = sqrt(subsigtrial)
c To prevent sigtrial =0	   
       if(sigtrial.lt.Tol .and. sigtrial.ge.zero) sigtrial = Tol
       if(sigtrial.gt.(zero-Tol) .and. sigtrial.le.zero) then
          sigtrial = zero-Tol
       endif
C Update temperature    
       T= stateOld(i,3)
       if(T.le.Tol .and. T.ge.(zero-Tol)) then
         T = T0 + (Delta/(Dens*Cp))*radius*deqplas/facDctDamDev
       else 
         T = T + (Delta/(Dens*Cp))*radius*deqplas/facDctDamDev
       endif 
       facT = cT1*exp(zero-cT2*T)+cT3	   
C Update strain rate	 
       StraRate= stateOld(i,5)
       Acincr = stateOld(i,8)
       Sumstrainincr = stateOld(i,9)
       Sumtimeincr = stateOld(i,10)
       Avestrainincr = stateOld(i,11)
       if(StraRate.le.Tol .and. StraRate.ge.(zero-Tol)) then
          StraRate = StraRate0
       else 
        Acincr = Acincr + one
        Sumstrainincr = Sumstrainincr + deqplas
        Sumtimeincr = Sumtimeincr + dt
        if(Nrincr.gt.half .and. Nrincr.lt.(one+half))then
          StraRate = deqplas/dt
          Avestrainincr = deqplas
        else
          StraRate = (Sumstrainincr/Sumtimeincr + StraRate)/two
          Avestrainincr = (Sumstrainincr/Acincr + Avestrainincr)/two
          if(Acincr.gt.(Nrincr-half) .and. Acincr.lt.(Nrincr+half))then
            Acincr = zero
            Sumstrainincr = zero
            Sumtimeincr = zero
          endif
        endif  
       endif 
       facStraRateM = cE1*log(StraRate)+cE2 
       facStraRateA = cE3*(StraRate)	   
       if(facStraRateM.lt.one) then
          facStraRateM = one
       endif
       StraRatRT = deqplas/dt
C Calculate mean stress and deviatoric stress components
       sigmean = third * StressTrace
       dsig1 = ST1 - sigmean
       dsig2 = ST2 - sigmean
       dsig3 = ST3 - sigmean
C Calculate the magnitude of the deviatoric trial stress tensor 	
       dsigmag=sqrt(dsig1**2+dsig2**2+dsig3**2+two*ST4**2+two*ST5**2+
     1	            two*ST6**2)
c To prevent dsigmag =0
       if(dsigmag.lt.Tol .and. dsigmag.ge.zero) dsigmag = Tol
       if(dsigmag.gt.(zero-Tol) .and. dsigmag.le.zero) dsigmag=zero-Tol	   	   
C Calculate the Mises equivalent stress 
       SigMises = const1*dsigmag
C Calculate the stress triaxiality	   
       Eta = sigmean/SigMises
C Calculate the 3rd invariant of the stress tensor
       r = (three/twoThirds*(dsig1*(dsig1**2+ST4**2+ST5**2)
     1    +two*ST4*(dsig1*ST4+dsig2*ST4+ST5*ST6)
     1	  +two*ST5*(dsig1*ST5+ST4*ST6+dsig3*ST5)
     1    +dsig2*(ST4**2+dsig2**2+ST6**2)
     1    +two*ST6*(ST4*ST5+dsig2*ST6+dsig3*ST6)
     1    +dsig3*(ST5**2+ST6**2+dsig3**2)))**third
       cosine = (r/SigMises)**3
c Assuring that -1<cosine<1
       if (cosine.gt.one) cosine=one
       if (cosine.lt.(zero-one)) cosine=zero-one
C Calculate the Lode angle and the normalized Lode angle
       Theta = third*acos(cosine)	  
       Thetabar = one - six*Theta/PI
C Determine the initial fracture indication flag (zero means no damage)
       Fracflag = stateOld(i,29)
       if(Fracflag.le.Tol .and. Fracflag.ge.(zero-Tol)) then
       Fracflag = zero
       endif	   
C Calculate the equivalent plastic strain to cleavage fracture
      Epscf=(Cc1*exp(zero-Cc2*Eta)-Cc3*exp(zero-Cc4*Eta))*(Thetabar**2)
     1	   +Cc3*exp(zero-Cc4*Eta)
C Calculate the equivalent plastic strain based cleavage fracture indicator
       AAAB = stateOld(i,15)
       AAAB = AAAB + deqplas/Epscf
C Calculate the equivalent plastic strain to damage initiation
       Epsddi=(half*(Ddi1*exp(zero-Ddi2*Eta)+Ddi5*exp(zero-Ddi6*Eta))-
     1 Ddi3*exp(zero-Ddi4*Eta))*(Thetabar**2)
     1 +half*(Ddi1*exp(zero-Ddi2*Eta)-Ddi5*exp(zero-Ddi6*Eta))*Thetabar
     1 +Ddi3*exp(zero-Ddi4*Eta)	  
C Calculate the ductile damage initiation indicator
c Ductile damage initiation is suppressed when Eta<Cut-off value 
       BBBB = stateOld(i,16)
!       if(BBBB.le.Tol .and. BBBB.ge.(zero-Tol)) then
!       BBBB = zero
!       endif
       if(Eta.lt.Cut) then
       BBBB = BBBB
       endif
       dBBBB = deqplas/Epsddi
       if(Eta.ge.Cut) then
       BBBB = BBBB+dBBBB
       endif
C Determine the fracture indication flag (one means ductile damage)	   
       if(BBBB.ge.one) then
       BBBB = one
       Fracflag = one
       endif	   
C Calculate the critical ductile damage variable    
      Dcrit=(Dc1*exp(zero-Dc2*Eta)-Dc3*exp(zero-Dc4*Eta))*(Thetabar**2)
     1	    +Dc3*exp(zero-Dc4*Eta)
C Calculate the ductile fracture indicator 
       BBB=stateOld(i,17)
       Damage= stateOld(i,18)	   
       if(BBB.le.Tol .and. BBB.ge.(zero-Tol)) then
       BBB = zero
       endif 	
C Calculate the yield stress at the onset of ductile damage
       if(BBBB.ge.one .and. eqplas.gt.Tol) then
         Sigdi=stateOld(i,27)
         Epsdi=stateOld(i,28)
        if (stateOld(i,31).le.Tol) then
c Store the yield stress at the onset of damage for the first time		
           Sigdi=radius
           Epsdi=eqplas
           stateNew(i,31) = one
        else
c Keep the yield stress at the onset of damage unchanged
           Sigdi=Sigdi
           Epsdi=Epsdi
        endif 
c Elements under hydrostatic compression don't experience spherical damage
        if(Eta.lt.Cut .and. BBB.lt.one) then
           BBB=BBB
           dBBB=zero
           Damage= Damage
           dDamage = zero		   
        else
           dBBB=Sigdi*deqplas/(Gf*Dcrit)
           BBB=BBB+dBBB
           dDamage=Sigdi*deqplas/(Gf)
           Damage=Damage+dDamage
        endif
c Determine the fracture indication flag (two means ductile fracture)		
        if(BBB.gt.one) then
          BBB=one
          dBBB=zero
          Fracflag = two
        endif
      else	
C In case no damage is reached, the yield stress at the onset of ductile
c damage and damage variable are unchanged
       Sigdi=Sigdi
       Epsdi=Epsdi
       BBBB=BBBB
       BBB=zero	
       Damage=zero
       dDamage=zero
      endif	
C Update the damage solftening factor
      if(BBB.ge.one) then
       BBB=one
       dDamage = zero
       facDctDamDev=zero
       facDctDamVol=zero
       dfacDctDamDev=zero
       Fracflag = two
       Deletion = zero
      else
       facDctDamDev= one - Damage
       facDctDamVol=facDctDamDev
       dfacDctDamDev=zero-dDamage
      endif	
C Update trial stress with new damage variable dfacDctDamDev
      STRESST(1)=stressOld(i,1)+(DDSDDE(1,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(1,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(1,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(1,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(1,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(1,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(2)=stressOld(i,2)+(DDSDDE(2,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(2,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(2,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(2,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(2,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(2,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev	  
      STRESST(3)=stressOld(i,3)+(DDSDDE(3,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(3,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(3,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(3,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(3,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(3,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(4)=stressOld(i,4)+(DDSDDE(4,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(4,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(4,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(4,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(4,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(4,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(5)=stressOld(i,5)+(DDSDDE(5,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(5,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(5,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(5,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(5,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(5,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev
      STRESST(6)=stressOld(i,6)+(DDSDDE(6,1)*(DSTRAN(1)-dgama*dgds(1))
     1          +DDSDDE(6,2)*(DSTRAN(2)-dgama*dgds(2))
     1          +DDSDDE(6,3)*(DSTRAN(3)-dgama*dgds(3))
     1          +DDSDDE(6,4)*(DSTRAN(4)-dgama*dgds(4))
     1          +DDSDDE(6,5)*(DSTRAN(5)-dgama*dgds(5))
     1          +DDSDDE(6,6)*(DSTRAN(6)-dgama*dgds(6)))*facDctDamDev	  
C Update stress tensors
       ST1=STRESST(1)
       ST2=STRESST(2)
       ST3=STRESST(3)
       ST4=STRESST(4)
       ST5=STRESST(5)
       ST6=STRESST(6)
       StressTrace = ST1 + ST2 + ST3
C Update the invariants of stress tensor
       StrInva1 = StressTrace
       StrInva2 = ST1*ST2-ST4*ST4+ST1*ST3-ST6*ST6+ST2*ST3-ST5*ST5
       StrInva3 = ST1*(ST2*ST3-ST6*ST6)-ST4*(ST4*ST3-ST6*ST5)+ST5*
     1	         (ST4*ST6-ST2*ST5)
C Calculate the subvalues for principal stress determination
       cosine2 = (two*StrInva1*StrInva1*StrInva1-three*three*StrInva1
     1 	*StrInva2+three*three*three*StrInva3)/(two*(StrInva1*StrInva1
     1	-three*StrInva2)**(threeHalves))
c Assuring that -1<cosine2<1
       if (cosine2.gt.one) cosine2=one
       if (cosine2.lt.(zero-one)) cosine2=zero-one
       alpha2 = acos(cosine2)
C Calculating the principal stress values
       SP1 = StrInva1/three + twoThirds*sqrt(StrInva1*StrInva1-three*
     1       StrInva2)*cos(alpha2/three)
       SP2 = StrInva1/three + twoThirds*sqrt(StrInva1*StrInva1-three*
     1	     StrInva2)*cos(alpha2/three+twoThirds*PI)
       SP3 = StrInva1/three + twoThirds*sqrt(StrInva1*StrInva1-three*
     1	   StrInva2)*cos(twoThirds*PI-alpha2/three)
C Fetching the maximum of the principal stress values
       Sigmamax = max(abs(SP1),abs(SP2),abs(SP3))
C Cleavage fracture
C Maximum principal stress criterion
       AAAA = stateOld(i,14)
       if (Sigmamax.ge.Sigcf .and. eqplas.gt.zero) then
          AAAA = one
       else
          AAAA = zero
       endif
C Cleavage fracture with both stress and strain criteria
       AAA = stateOld(i,13)
       if(AAAB.ge.one .and. eqplas.gt.zero) then
         if (AAAA.ge.one .and. eqplas.gt.zero) then
           STRESST(1) = zero
           STRESST(2) = zero
           STRESST(3) = zero
           STRESST(4) = zero
           STRESST(5) = zero
           STRESST(6) = zero
           Fracflag = three
           AAA = one
           Deletion = zero
           goto 9000
         endif
       endif
       ST1=STRESST(1)
       ST2=STRESST(2)
       ST3=STRESST(3)
       ST4=STRESST(4)
       ST5=STRESST(5)
       ST6=STRESST(6)	
C Check yielding at new quivalent plastic strain and new correction factors
C Update subvalue of the trial Hill48 equivalent stress	
       subsigtrial = F*(ST2-ST3)**2+G*(ST3-ST1)**2+H*(ST1-ST2)**2+
     1	               two*N*ST4**2+two*L*ST5**2+two*M*ST6**2
c To prevent subsigtrial =0
       if(subsigtrial.lt.Tol) subsigtrial = Tol	 
C Update the trial Hill48 equivalent stress 
       sigtrial = sqrt(subsigtrial)
c To prevent sigtrial =0
       if(sigtrial.lt.Tol .and. sigtrial.ge.zero) sigtrial = Tol
       if(sigtrial.gt.(zero-Tol) .and. sigtrial.le.zero) then
          sigtrial = zero-Tol
       endif	   
C Update the radius	   
       radius=(sigmayield*facStraRateM+facStraRateA)*facT*facDctDamDev
       Xhardnew=(xhard)*facStraRateM*facT*facDctDamDev	   
       xf = sigtrial - radius
C Check if the stress state is located on the updated yield loci
      if(iflag.gt.(one-Tol)) then
         goto 1000
      endif
      if(xf.le.Tol .and. xf.ge.(zero-Tol)) then
         goto 1000
      else 
         goto 5000
      endif		   
c
1000  continue
C     Update PEEQ		 
      stateNew(i,1) = eqplas
c      write(*,*) "stateNew(i,1)", stateNew(i,1)
C     Update equivalent stress
      stateNew(i,2) = sigtrial	 
C     Update TmP
      stateNew(i,3) = T
      stateNew(i,4) = facT
C     Update StrainRate
      stateNew(i,5) = StraRate
      stateNew(i,6) = facStraRateM
      stateNew(i,7) = facStraRateA	
      stateNew(i,8) = Acincr
      stateNew(i,9) = Sumstrainincr
      stateNew(i,10) = Sumtimeincr
      stateNew(i,11) =	Avestrainincr 
      stateNew(i,12) =	StraRatRT
C     Update Damage variable
      stateNew(i,13) = AAA
      stateNew(i,14) = AAAA
      stateNew(i,15) = AAAB
      stateNew(i,16) = BBBB
      stateNew(i,17) = BBB
      stateNew(i,18) = Damage
C     Update stress state parameters
      stateNew(i,19) = SigMises
      stateNew(i,20) = Eta
      stateNew(i,21) = Theta
      stateNew(i,22) = Thetabar
C     Update damage related parameters
      stateNew(i,23) = Epscf
      stateNew(i,24) = Epsddi
      stateNew(i,25) = Dcrit
      stateNew(i,26) = Sigmamax
      stateNew(i,27) = Sigdi
      stateNew(i,28) = Epsdi
      stateNew(i,29) = Fracflag
      stateNew(i,30) = Deletion	  	  
C     Update stress
      DO 180 K1=1,NTENS          
         stressNew(i,K1)=STRESST(K1)
180   CONTINUE
C   
9000  continue
      return
      end
c
      subroutine ahard(sigmayield0,hard0,sigmayield45,sigmayield90,sigmayieldEB,
     1	  rvalue0,rvalue45,rvalue90,eqplas,table,nvalue)
C
      include 'vaba_param.inc'
      dimension table(8,nvalue)
C
C     Set yield stress to second value of table, hardening to zero
      sigmayield0=table(2,nvalue)
      hard0=zero
      sigmayield45=table(3,nvalue)
      hard45=zero
      sigmayield90=table(4,nvalue)
      hard90=zero
      sigmayieldEB=table(5,nvalue)
	  hardEB=zero
      rvalue0=table(6,nvalue)
      hardr0=zero
      rvalue45=table(7,nvalue)
      hardr45=zero
      rvalue90=table(8,nvalue)
      hardr90=zero
C
C     If more than one entry, search table
      if(nvalue.gt.1) then
        do 10 k1=1,nvalue-1
          eqpl1=table(1,k1+1)
          if(eqplas.lt.eqpl1) then
            eqpl0=table(1,k1)
            if(eqpl1.le.eqpl0) then
              write(6,7)
 7            format(//,30X,'***ERROR - PLASTIC STRAIN MUST BE ',
     1               'ENTERED IN ASCENDING ORDER,')
C
C             Subroutine XIT terminates execution and closes all files
              call XIT
            endif
            deqpl=eqpl1-eqpl0
            sigmayield0a=table(2,k1)
            sigmayield0b=table(2,k1+1)
            dsigmayield0=sigmayield0b-sigmayield0a
            hard0=dsigmayield0/deqpl
            sigmayield0=sigmayield0a+(eqplas-eqpl0)*hard0
            sigmayield45a=table(3,k1)
            sigmayield45b=table(3,k1+1)
            dsigmayield45=sigmayield45b-sigmayield45a
            hard45=dsigmayield45/deqpl
            sigmayield45=sigmayield45a+(eqplas-eqpl0)*hard45
            sigmayield90a=table(4,k1)
            sigmayield90b=table(4,k1+1)
            dsigmayield90=sigmayield90b-sigmayield90a
            hard90=dsigmayield90/deqpl
            sigmayield90=sigmayield90a+(eqplas-eqpl0)*hard90
            sigmayieldEBa=table(5,k1)
            sigmayieldEBb=table(5,k1+1)
            dsigmayieldEB=sigmayieldEBb-sigmayieldEBa
            hardEB=dsigmayieldEB/deqpl
            sigmayieldEB=sigmayieldEBa+(eqplas-eqpl0)*hardEB
            rvalue0a=table(6,k1)
            rvalue0b=table(6,k1+1)
            drvalue0=rvalue0b-rvalue0a
            hardr0=drvalue0/deqpl
            rvalue0=rvalue0a+(eqplas-eqpl0)*hardr0
            rvalue45a=table(7,k1)
            rvalue45b=table(7,k1+1)
            drvalue45=rvalue45b-rvalue45a
            hardr45=drvalue45/deqpl
            rvalue45=rvalue45a+(eqplas-eqpl0)*hardr45
            rvalue90a=table(8,k1)
            rvalue90b=table(8,k1+1)
            drvalue90=rvalue90b-rvalue90a
            hardr90=drvalue90/deqpl
            rvalue90=rvalue90a+(eqplas-eqpl0)*hardr90			
            goto 20
          endif
 10     continue
 20     continue
        if(eqplas.gt.table(1,nvalue)) then
          hard0=(table(2,nvalue)-table(2,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          sigmayield0=table(2,nvalue)+(eqplas-table(1,nvalue))*hard0
          hard45=(table(3,nvalue)-table(3,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          sigmayield45=table(3,nvalue)+(eqplas-table(1,nvalue))*hard45
          hard90=(table(4,nvalue)-table(4,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          sigmayield90=table(4,nvalue)+(eqplas-table(1,nvalue))*hard90
          hardEB=(table(5,nvalue)-table(5,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          sigmayieldEB=table(5,nvalue)+(eqplas-table(1,nvalue))*hardEB
          hardr0=(table(6,nvalue)-table(6,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          rvalue0=table(6,nvalue)+(eqplas-table(1,nvalue))*hardr0
          hardr45=(table(7,nvalue)-table(7,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          rvalue45=table(7,nvalue)+(eqplas-table(1,nvalue))*hardr45
          hardr90=(table(8,nvalue)-table(8,nvalue-1))
     1        /(table(1,nvalue)-table(1,nvalue-1))
          rvalue90=table(8,nvalue)+(eqplas-table(1,nvalue))*hardr90	  
        endif
      endif
      return
C
C Iteration ends here
      end  