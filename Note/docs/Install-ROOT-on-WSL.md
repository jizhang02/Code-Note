# Insatall ROOT on WSL
### Preface
#### 🧐 What is ROOT?
ROOT is a general data analysis framework developed by CERN. It is an object-oriented framework for storing, processing and visualizing large scientific data sets. ROOT can be used in a variety of scientific fields, including physics, astrophysics, biology, medicine, and more.
#### 🧐 What is SNAP?
In Linux, snap is a software package format developed by Ubuntu. Snap packages are self-contained, which means they contain all files and dependencies required by the application. This makes them easier to install and use, and more secure because they don't rely on other software on the system.

Install if it does not have in Ubuntu: `sudo apt install snapd`

After installation, use it by: `snap search <application>` `sudo snap install <application>`

### Install ROOT via SNAP
`sudo snap install root-framework`


### Analysis
* in terminal
  
`snap run root-framework` or `root`

`root pet.root` open a root file

`.ls` show info

`branch name->GetEntries()` number of events

`branch name->Show(eventid)` info of an event

`.q` exit

`TBrowser b` open a interactive browser

#### Check hits info

```
root g9_point_2head_0.5s_c.root  // open a root file
.ls                              // show branches info
TFile**         g9_point_2head_0.5s_c.root      ROOT file with histograms
 TFile*         g9_point_2head_0.5s_c.root      ROOT file with histograms
  OBJ: TTree    Hits    The root tree for hits : 0 at: 0x562f4f487cf0
  OBJ: TTree    Singles The root tree for singles : 0 at: 0x562f51694340
  OBJ: TTree    Coincidences    The root tree for coincidences : 0 at: 0x562f5145baa0
  KEY: TH1D     latest_event_ID;1       latest_event_ID(#)
  KEY: TH1D     total_nb_primaries;1    total_nb_primaries(#)
  KEY: TTree    pet_data;1      data for PET analysis
  KEY: TTree    Hits;1  The root tree for hits
  KEY: TTree    OpticalData;1   OpticalData
  KEY: TTree    Coincidences;1  The root tree for coincidences
  KEY: TTree    Singles;1       The root tree for singles
Hits->Show()                     // show Hits first event
Hits->Show(10)                   // show Hits 10th event
Hits->GetEntries()               // (long long) 176124
Hits->Print()                    // the number of entries, the branches and the leaves
******************************************************************************
*Tree    :Hits      : The root tree for hits                                 *
*Entries :   176124 : Total =        42275828 bytes  File  Size =    9864992 *
*        :          : Tree compression factor =   4.29                       *
******************************************************************************
*Br    0 :PDGEncoding : PDGEncoding/I                                        *
*Entries :   176124 : Total  Size=     722175 bytes  File Size  =      50439 *
*Baskets :      177 : Basket Size=       4096 bytes  Compression=  14.24     *
*............................................................................*
*Br    1 :trackID   : trackID/I                                              *
*Entries :   176124 : Total  Size=     721451 bytes  File Size  =     114333 *
*Baskets :      177 : Basket Size=       4096 bytes  Compression=   6.28     *
*............................................................................*
*Br    2 :parentID  : parentID/I                                             *
*Entries :   176124 : Total  Size=     721632 bytes  File Size  =      57657 *
*Baskets :      177 : Basket Size=       4096 bytes  Compression=  12.45     *
*............................................................................*

Hits->Scan()                     // will print the first 8 variables of the tree
************************************************************************************************************
*    Row   * PDGEncodi * trackID.t * parentID. * trackLoca * time.time * edep.edep * stepLengt * trackLeng *
************************************************************************************************************
*        0 *       -11 *         1 *         0 * 9.125e-10 * 0.0006236 * 0.0043947 * 0.0083140 * 235.34182 *
*        1 *       -11 *         1 *         0 * 9.125e-10 * 0.0006236 * 0.0057441 * 0.0105544 * 235.35238 *
*        2 *       -11 *         1 *         0 * 9.126e-10 * 0.0006236 * 0.0074570 * 0.0105038 * 235.36288 *
*        3 *       -11 *         1 *         0 * 9.126e-10 * 0.0006236 * 0.0052258 * 0.0135401 * 235.37641 *
*        4 *       -11 *         1 *         0 * 9.127e-10 * 0.0006236 * 0.0208282 * 0.0249958 * 235.40142 *
*        5 *       -11 *         1 *         0 * 9.128e-10 * 0.0006236 * 0.0243323 * 0.0316746 * 235.43309 *
*        6 *       -11 *         1 *         0 * 9.129e-10 * 0.0006236 * 0.0323055 * 0.0472882 * 235.48037 *
*        7 *       -11 *         1 *         0 * 9.130e-10 * 0.0006236 * 0.0512420 * 0.0654094 * 235.54579 *
*        8 *       -11 *         1 *         0 * 9.131e-10 * 0.0006236 * 0.0301794 * 0.0276358 * 235.57342 *
*        9 *       -11 *         1 *         0 * 9.132e-10 * 0.0006236 * 0.0803841 * 0.0230165 * 235.59645 *
*       10 *       -11 *         1 *         0 * 9.132e-10 * 0.0006236 * 0.0477072 * 0.0282339 * 235.62468 *

Type <CR> to continue or q to quit ==>

Hits->Scan("*")                     // will print all the variables of the tree.
***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
*    Row   * Instance * PDGEncodi * trackID.t * parentID. * trackLoca * time.time * edep.edep * stepLengt * trackLeng * posX.posX * posY.posY * posZ.posZ * localPosX * localPosY * localPosZ * momDirX.m * momDirY.m * momDirZ.m * gantryID. * blockID.b * crystalID * unused3ID * unused4ID * unused5ID * photonID. * nPhantomC * nCrystalC * nPhantomR * nCrystalR * primaryID * sourcePos * sourcePos * sourcePos * sourceID. * eventID.e * runID.run * axialPos. * rotationA * volumeID. * processNa * comptVolN * RayleighV * sourceTyp * decayType * gammaType *
***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
*        0 *        0 *       -11 *         1 *         0 * 9.125e-10 * 0.0006236 * 0.0043947 * 0.0083140 * 235.34182 * -228.0073 * -23.62822 * -8.239537 * -9.992618 * 23.628223 * -8.239537 * -0.938055 * 0.2813308 * -0.202250 *         0 *         1 *         0 *        -1 *        -1 *        -1 *         0 *         0 *         0 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *

Hits->SetScanField(0)               // all rows are shown
Hits->SetScanField(50)              // 50 rows are shown
Hits->Show(0)                       // show the 1st event
======> EVENT:0
 PDGEncoding     = -11
 trackID         = 1
 parentID        = 0
 trackLocalTime  = 9.12548e-10
 time            = 0.000623619
 edep            = 0.00439479
 stepLength      = 0.00831402
 trackLength     = 235.342
 posX            = -228.007
 posY            = -23.6282
 posZ            = -8.23954
 localPosX       = -9.99262
 localPosY       = 23.6282
 localPosZ       = -8.23954
 momDirX         = -0.938055
 momDirY         = 0.281331
 momDirZ         = -0.20225
 gantryID        = 0
 blockID         = 1
 crystalID       = 0
 unused3ID       = -1
 unused4ID       = -1
 unused5ID       = -1
 photonID        = 0
 nPhantomCompton = 0
 nCrystalCompton = 0
 nPhantomRayleigh = 0
 nCrystalRayleigh = 0
 primaryID       = 1
 sourcePosX      = 0
 sourcePosY      = 0
 sourcePosZ      = 0
 sourceID        = 0
 eventID         = 603
 runID           = 0
 axialPos        = 0
 rotationAngle   = 0
 volumeID        = 0,
                  0, 1, 0, -1, -1, -1, -1, -1, -1
 processName     = msc
 comptVolName    = NULL
 RayleighVolName = NULL
 sourceType      = 0
 decayType       = 0
 gammaType       = 0

Hits->Scan("trackID:parentID:time:edep:blockID:crystalID:photonID:primaryID:nPhantomCompton:nCrystalCompton:nPhantomRayleigh:nCrystalRayleigh:decayType:processName")
************************************************************************************************************************************************************************************
*    Row   *   trackID *  parentID *      time *      edep *   blockID * crystalID *  photonID * primaryID * nPhantomC * nCrystalC * nPhantomR * nCrystalR * decayType * processNa *
************************************************************************************************************************************************************************************
*        0 *         1 *         0 * 0.0006236 * 0.0043947 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        1 *         1 *         0 * 0.0006236 * 0.0057441 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        2 *         1 *         0 * 0.0006236 * 0.0074570 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        3 *         1 *         0 * 0.0006236 * 0.0052258 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        4 *         1 *         0 * 0.0006236 * 0.0208282 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        5 *         1 *         0 * 0.0006236 * 0.0243323 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        6 *         1 *         0 * 0.0006236 * 0.0323055 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        7 *         1 *         0 * 0.0006236 * 0.0512420 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        8 *         1 *         0 * 0.0006236 * 0.0301794 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*        9 *         1 *         0 * 0.0006236 * 0.0803841 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*       10 *         1 *         0 * 0.0006236 * 0.0477072 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *       msc *
*       11 *         1 *         0 * 0.0006236 * 0.1098842 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       12 *         1 *         0 * 0.0006236 *         0 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *   annihil *
*       13 *       113 *         1 * 0.0006236 * 0.5109989 *         1 *         0 *         1 *         1 *         0 *         0 *         0 *         0 *         0 *      phot *
*       14 *       111 *         1 * 0.0006236 * 9.493e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       15 *       110 *         1 * 0.0006236 * 8.782e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       16 *       109 *         1 * 0.0006236 * 8.782e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       17 *       108 *         1 * 0.0006236 * 8.782e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       18 *       107 *         1 * 0.0006236 * 8.782e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       19 *       106 *         1 * 0.0006236 * 8.071e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       20 *       105 *         1 * 0.0006236 * 9.493e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       21 *       104 *         1 * 0.0006236 * 2.993e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       22 *       103 *         1 * 0.0006236 * 9.557e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       23 *       102 *         1 * 0.0006236 * 2.925e-05 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
*       24 *       101 *         1 * 0.0006236 * 0.0004938 *         1 *         0 *         0 *         1 *         0 *         0 *         0 *         0 *         0 *     eIoni *
Type <CR> to continue or q to quit ==>
```
* `msc` (Multiple Scattering)
* `eIoni` (Electron Ionization)
* `annihil` (Electron-Positron Annihilation)
* `phot` (Photoelectric Effect)

#### Check singles info
```
Singles->Show(0)                 // show Singles 1st event
======> EVENT:0
 runID           = 0
 eventID         = 702
 sourceID        = 0
 sourcePosX      = 0
 sourcePosY      = 0
 sourcePosZ      = 0
 time            = 0.000727677
 energy          = 0.548263
 globalPosX      = 233.749
 globalPosY      = -17.7768
 globalPosZ      = 10.3119
 gantryID        = 0
 blockID         = 0
 crystalID       = 0
 unused3ID       = -1
 unused4ID       = -1
 unused5ID       = -1
 comptonPhantom  = 0
 comptonCrystal  = 1
 RayleighPhantom = 0
 RayleighCrystal = 0
 axialPos        = 0
 rotationAngle   = 0
 comptVolName    = NULL
 RayleighVolName = NULL
 volumeID        = 0,
                  0, 0, 0, -1, -1, -1, -1, -1, -1

Singles->Scan("eventID:time:energy:blockID:crystalID:comptonPhantom:comptonCrystal:RayleighPhantom:RayleighCrystal:comptVolName:RayleighVolName:volumeID")
***********************************************************************************************************************************************************************
*    Row   * Instance *   eventID *      time *    energy *   blockID * crystalID * comptonPh * comptonCr * RayleighP * RayleighC * comptVolN * RayleighV *  volumeID *
***********************************************************************************************************************************************************************
*        0 *        0 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *      NULL *      NULL *         0 *
*        0 *        1 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *         0 *
*        0 *        2 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *         0 *
*        0 *        3 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *         0 *
*        0 *        4 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        0 *        5 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        0 *        6 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        0 *        7 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        0 *        8 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        0 *        9 *       702 * 0.0007276 * 0.5482634 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        1 *        0 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *      NULL *      NULL *         0 *
*        1 *        1 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *         0 *
*        1 *        2 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *         0 *
*        1 *        3 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *         0 *
*        1 *        4 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        1 *        5 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        1 *        6 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        1 *        7 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        1 *        8 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        1 *        9 *      1030 * 0.0010454 * 0.5109989 *         0 *         0 *         0 *         1 *         0 *         0 *           *           *        -1 *
*        2 *        0 *      1179 * 0.0011952 * 0.5109989 *         0 *         0 *         0 *         0 *         0 *         0 *      NULL *      NULL *         0 *
*        2 *        1 *      1179 * 0.0011952 * 0.5109989 *         0 *         0 *         0 *         0 *         0 *         0 *           *           *         0 *
*        2 *        2 *      1179 * 0.0011952 * 0.5109989 *         0 *         0 *         0 *         0 *         0 *         0 *           *           *         0 *
*        2 *        3 *      1179 * 0.0011952 * 0.5109989 *         0 *         0 *         0 *         0 *         0 *         0 *           *           *         0 *
*        2 *        4 *      1179 * 0.0011952 * 0.5109989 *         0 *         0 *         0 *         0 *         0 *         0 *           *           *        -1 *
Type <CR> to continue or q to quit ==>
```
#### Check coincidences info
```
Coincidences->Show()             // show info
======> EVENT:-1
 runID           = 0
 axialPos        = 0
 rotationAngle   = 0
 eventID1        = 0
 sourceID1       = 0
 sourcePosX1     = 0
 sourcePosY1     = 0
 sourcePosZ1     = 0
 time1           = 0
 energy1         = 0
 globalPosX1     = 0
 globalPosY1     = 0
 globalPosZ1     = 0
 gantryID1       = 0
 blockID1        = 0
 crystalID1      = 0
 unused3ID1      = 0
 unused4ID1      = 0
 unused5ID1      = 0
 comptonPhantom1 = 0
 comptonCrystal1 = 0
 RayleighPhantom1 = 0
 RayleighCrystal1 = 0
 eventID2        = 0
 sourceID2       = 0
 sourcePosX2     = 0
 sourcePosY2     = 0
 sourcePosZ2     = 0
 time2           = 0
 energy2         = 0
 globalPosX2     = 0
 globalPosY2     = 0
 globalPosZ2     = 0
 gantryID2       = 0
 blockID2        = 0
 crystalID2      = 0
 unused3ID2      = 0
 unused4ID2      = 0
 unused5ID2      = 0
 comptonPhantom2 = 0
 comptonCrystal2 = 0
 RayleighPhantom2 = 0
 RayleighCrystal2 = 0
 sinogramTheta   = 0
 sinogramS       = 0
 comptVolName1   =
 comptVolName2   =
 RayleighVolName1 =
 RayleighVolName2 =

Coincidences->Scan("eventID1:eventID2:time1:time2:energy1:energy2:blockID1:blockID2:crystalID1:crystalID2:globalPosX1:globalPosX2:globalPosY1:globalPosY2")
************************************************************************************************************************************************************************************
*    Row   *  eventID1 *  eventID2 *     time1 *     time2 *   energy1 *   energy2 *  blockID1 *  blockID2 * crystalID * crystalID * globalPos * globalPos * globalPos * globalPos *
************************************************************************************************************************************************************************************
*        0 *        11 *        11 * 1.444e-05 * 1.444e-05 * 0.5324218 * 0.5109989 *       177 *       160 *       125 *        93 * -187.0208 * -171.6790 * -386.1606 * 394.42157 *
*        1 *        37 *        37 * 3.531e-05 * 3.531e-05 * 0.5109989 * 0.5109989 *         1 *        19 *        60 *         5 * 432.11505 * -315.9100 * 30.950630 * 290.17877 *
*        2 *        53 *        53 * 5.174e-05 * 5.174e-05 * 0.5109989 * 0.5109989 *        43 *       183 *       125 *       148 * 334.40533 * 132.85568 * -288.0577 * -417.7819 *
*        3 *        89 *        89 * 7.946e-05 * 7.946e-05 * 0.4837822 * 0.5109989 *        25 *       108 *        55 *        38 * -428.2357 * 6.4320244 * -10.90172 * 432.43249 *
*        4 *       317 *       317 * 0.0003166 * 0.0003166 * 0.5109989 * 0.5109989 *       174 *         5 *        66 *        77 * -348.9855 * 361.67471 * -271.7265 * 264.57934 *
*        5 *       369 *       369 * 0.0003869 * 0.0003869 * 0.5371779 * 0.5109989 *       112 *        30 *        88 *        37 * -202.5240 * -318.0317 * 387.48617 * -299.8047 *
*        6 *       432 *       432 * 0.0004504 * 0.0004504 * 0.5109989 * 0.5109989 *        45 *       165 *       125 *        36 * 396.68466 * -392.3652 * -191.1926 * 178.15414 *
*        7 *       452 *       452 * 0.0004728 * 0.0004728 * 0.5109989 * 0.5109989 *       136 *       158 *        62 *        91 * 208.82975 * -56.68589 * -394.8935 * 426.40594 *
*        8 *       462 *       463 * 0.0004833 * 0.0004834 * 0.5109989 * 0.5109989 *       150 *        81 *        62 *        23 * 316.24096 * -186.2989 * 294.26141 * -406.7476 *
*        9 *       668 *       668 * 0.0006950 * 0.0006950 * 0.5109989 * 0.5109989 *        34 *       104 *        22 *        73 * -131.6641 * 241.90921 * -408.7626 * 367.69650 *
*       10 *       681 *       681 * 0.0007096 * 0.0007096 * 0.5109989 * 0.5109989 *       124 *        52 *         7 *       148 * -397.0189 * 402.22509 * -196.1065 * 187.52545 *
*       11 *       689 *       689 * 0.0007183 * 0.0007183 * 0.6355064 * 0.5109989 *       159 *       148 *       110 *       138 * -136.7851 * 387.73083 * 413.18487 * 193.55830 *
*       12 *       706 *       706 * 0.0007394 * 0.0007394 * 0.5109989 * 0.5109989 *         0 *       118 *       111 *        43 * 446.05719 * -407.2573 * -27.57494 *  149.8591 *
*       13 *       736 *       736 * 0.0007659 * 0.0007659 * 0.5109989 * 0.5109989 *       111 *       140 *         5 *       151 * -135.1369 * 364.78491 * 423.58474 * -240.9290 *
*       14 *       763 *       763 * 0.0007981 * 0.0007981 * 0.5109989 * 0.5109989 *       163 *        28 *        62 *       162 * -335.2828 * -394.2877 * 277.23571 * -189.8426 *
*       15 *       809 *       810 * 0.0008427 * 0.0008427 * 0.5109989 * 0.5109989 *       132 *        52 *        45 *        75 * -31.34817 * 390.03521 * -441.4894 * 207.18399 *
*       16 *       853 *       853 * 0.0008851 * 0.0008851 * 0.5109989 * 0.5109989 *        66 *       186 *        14 *       143 * -272.5115 * 271.42819 * 344.64590 * -349.7161 *
*       17 *       903 *       903 * 0.0009330 * 0.0009330 * 0.6458153 * 0.5109989 *       154 *       111 *        94 *       148 * 153.99688 * -131.2613 * 408.48764 * 407.69049 *
*       18 *       927 *       927 * 0.0009561 * 0.0009561 * 0.5109989 * 0.5109989 *        92 *        68 *        47 *       116 * 359.89111 * -382.4150 * -234.7964 * 231.95283 *
*       19 *       939 *       939 * 0.0009692 * 0.0009692 * 0.5109989 * 0.5109989 *       122 *       145 *       153 *        18 * -417.8856 * 437.05456 * -94.31806 * 21.063623 *
*       20 *       962 *       962 * 0.0009949 * 0.0009949 * 0.5109989 * 0.5109989 *         4 *        28 *        78 *       135 * 405.10965 * -391.7678 * 168.94775 * -185.0102 *
*       21 *       990 *       990 * 0.0010229 * 0.0010229 * 0.5109989 * 0.5109989 *        86 *       158 *         1 *        30 * 59.001098 * -73.46105 * -426.9371 * 428.90628 *
*       22 *      1143 *      1145 * 0.0011889 * 0.0011890 * 0.5109989 * 0.5109989 *       109 *        48 *        53 *       127 * -3.658747 * 440.71173 * 439.33352 * -16.71529 *
*       23 *      1154 *      1154 * 0.0011984 * 0.0011984 * 0.5109989 * 0.5109989 *       113 *       135 *       125 *        17 * -252.4592 * 126.57633 * 367.74322 * -412.4742 *
*       24 *      1207 *      1208 * 0.0012541 * 0.0012541 * 0.5109989 * 0.5109989 *        73 *       136 *        98 *        73 * -442.3806 * 194.91403 * -29.86315 * -383.2742 *
Type <CR> to continue or q to quit ==>
```


* in Python
  
 `pyroot` (instead of `python`) `>>> import ROOT`

`pyroot root.py` but not really used 🪫

### Install uproot (Python lib) to read and write root files
🌟🌟🌟another way to read and write root file:    
`pip install uproot` [Tutorial](https://uproot.readthedocs.io/en/latest/basic.html)


#### Check singles info
```
import uproot
import numpy as np
np.set_printoptions(threshold=np.inf)  # No limit on the number of rows displayed when printing an array

filename = 'g10_b2b1s_2b_ewp.root'
file = uproot.open(filename)
for t in file: print(f'Tree {t}') # print the list of trees

hits = file['Hits']
singles = file['Singles1']
singles_ew= file['EnergyWindows']
print(f'Number of hits : {hits.num_entries}')
print(f'Number of singles : {singles.num_entries}')
print(f'Number of singles(ew) : {singles_ew.num_entries}')

# print branches in the singles tree
branches = singles_ew.keys()
print('Branches in Tree EnergyWindows:')
print(", ".join(branches))

chunk_size = 100
start = 0
data = singles_ew.arrays(branches, entry_start=start, entry_stop=start+chunk_size)

Energy = data['TotalEnergyDeposit']
PreStepUniqueVolumeID = data['PreStepUniqueVolumeID']
eventID = data['EventID']
PostPosition_X = data['PostPosition_X']
PostPosition_Y = data['PostPosition_Y']
PostPosition_Z = data['PostPosition_Z']
EventPostPosition_X = data['EventPosition_X']
EventPostPosition_Y = data['EventPosition_Y']
EventPostPosition_Z = data['EventPosition_Z']
GlobalTime = data['GlobalTime']

for i in range(20):
    print(f"EventID: {eventID[i]}, PostPosition: ({PostPosition_X[i]:.0f} {PostPosition_Y[i]:.0f} {PostPosition_Z[i]:.0f}), EventPosition: ({EventPostPosition_X[i]:.0f} {EventPostPosition_Y[i]:.0f} {EventPostPosition_Z[i]:.0f}), PreStepUniqueVolumeID: {PreStepUniqueVolumeID[i]}, GlobalTime: {GlobalTime[i]:.2f}, Energy: {Energy[i]:.2f}")
```

The output is

```
Tree Hits;1
Tree Singles1;1
Tree Singles2;1
Tree EnergyWindows;1
Number of hits : 20825.0
Number of singles : 12043.0
Number of singles(ew) : 9645.0
Branches in Tree EnergyWindows:
EventID, EventPosition_X, EventPosition_Y, EventPosition_Z, GlobalTime, TotalEnergyDeposit, Position_X, Position_Y, Position_Z, PostPosition_X, PostPosition_Y, PostPosition_Z, PreStepUniqueVolumeID

EventID: 63, PostPosition: (238 0 0), EventPosition: (-3 3 -0), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 66370.18, Energy: 0.51
EventID: 96, PostPosition: (238 0 0), EventPosition: (-2 5 0), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 103747.27, Energy: 0.51
EventID: 96, PostPosition: (-238 0 0), EventPosition: (-2 5 0), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 103747.29, Energy: 0.51
EventID: 237, PostPosition: (-238 0 0), EventPosition: (-2 -1 -1), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 246700.00, Energy: 0.51
EventID: 331, PostPosition: (238 0 0), EventPosition: (3 -1 -3), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 334631.24, Energy: 0.51
EventID: 331, PostPosition: (-238 0 0), EventPosition: (3 -1 -3), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 334631.21, Energy: 0.51
EventID: 446, PostPosition: (238 0 0), EventPosition: (-0 0 -3), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 481740.14, Energy: 0.51
EventID: 565, PostPosition: (238 0 0), EventPosition: (-2 1 -3), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 600870.41, Energy: 0.51
EventID: 565, PostPosition: (-238 0 0), EventPosition: (-2 1 -3), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 600870.38, Energy: 0.51
EventID: 569, PostPosition: (238 0 0), EventPosition: (-1 4 1), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 602331.48, Energy: 0.51
EventID: 569, PostPosition: (-238 0 0), EventPosition: (-1 4 1), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 602331.51, Energy: 0.51
EventID: 676, PostPosition: (-238 0 0), EventPosition: (-1 0 0), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 695413.27, Energy: 0.51
EventID: 689, PostPosition: (-238 0 0), EventPosition: (-2 1 -1), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 709145.15, Energy: 0.51
EventID: 923, PostPosition: (238 0 0), EventPosition: (3 -1 1), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 930785.86, Energy: 0.51
EventID: 1103, PostPosition: (238 0 0), EventPosition: (4 -2 -1), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 1107056.36, Energy: 0.51
EventID: 1174, PostPosition: (238 0 0), EventPosition: (-3 0 3), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 1170443.74, Energy: 0.51
EventID: 1174, PostPosition: (-238 0 0), EventPosition: (-3 0 3), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 1170443.70, Energy: 0.51
EventID: 1186, PostPosition: (238 0 0), EventPosition: (4 2 2), PreStepUniqueVolumeID: 0_0_0_0_0, GlobalTime: 1180152.44, Energy: 0.51
EventID: 1186, PostPosition: (-238 0 0), EventPosition: (4 2 2), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 1180152.47, Energy: 0.51
EventID: 1250, PostPosition: (-238 0 0), EventPosition: (1 -3 3), PreStepUniqueVolumeID: 0_0_0_1_0, GlobalTime: 1251858.14, Energy: 0.51
```
