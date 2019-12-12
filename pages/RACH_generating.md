# RACH generating
## 生成 zaddoff chu 序列
Generate a Zaddoff Chu sequence (849 samples) using rootSequenceIndex (let's call this sequence as 'base sequence')  

![prach_zaddoff_chu_formula](http://taichiorange.github.io/images/lte_initial_attach/36_211_Zadoff_RACH.PNG)

Nzc indicate 'number of data in the ZaddOff Chu Sequence'. This number is fixed to be **839** in preamble format 0, 1,2,3 and **139** in preamble format 4, notes: format 4 is used only in TDD LTE. Refer to  table <36.211-Table 5.7.2-1: Random access preamble sequence length>  

u , 最大取值 837 ， as following in SIB2:
![prach_zaddoff_chu_u](http://taichiorange.github.io/images/lte_initial_attach/Root_Zadoff_Chu_sequence_order_for_preamble_formats_0to3.PNG)  

python 代码：  
[rach_zaddoff_generate](http://taichiorange.github.io/code/lte_prach/rach_zaddoff_chu_generate.py)

## 生成 64 个 preambles
There are 64 preambles available for each cell and UE has to be able to generate the 64 preambles for the cell it want to camp on.  

You can easily generate 64 different preambles just by cyclically shifting an existing sequence, but there is a condition for this. All the preamle sequences should be othogonal to each other. Otherwise, various preambles from multiple UEs within the same cell can interfere each other. So we have to shift the generated sequence by a specifically designed value and this value is called Cv (Cyclic Shift Value) and it is defined as follows. (I think determining the Cv is one of the most complicated process in PRACH preamble generation because it gets involved with so many different parameters in cascading manner).  

Cv 按照如下公式生成：

![prach_Cv](http://taichiorange.github.io/images/lte_initial_attach/PRACH_CyclicShift_Value.png)

### Ncs
![prach_Ncs](http://taichiorange.github.io/images/lte_initial_attach/PRACH_Ncs.png)


### 对于 unrestricted sets 情况
根据 Nzc 和 Ncs 就可以计算出来 Cv.    
> Ncs = 0 : Cv = 0  
> Ncs != 0: Cv = v 乘以 Cv, 其中， v 取值按照上图范围来取。  
？？？ 这里能保证得到 64 个 Cv 吗？  

### restricted sets 情况
这个情况复杂很多，需要知道如下四个数据：



[RRC]   radioResourceConfigCommon.rach_ConfigCommon.preambleInfo.numberOfRA_Preambles  : raw:15 decoded:n64  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.preambleInfo.preamblesGroupAConfig : not defined  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.powerRampingParameters.powerRampingStep                   : raw:2 decoded:dB4  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.powerRampingParameters.preambleInitialReceivedTargetPower : raw:6 decoded:dBm-108  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.ra_SupervisionInfo.preambleTransMax              : raw:6 decoded:n10  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.ra_SupervisionInfo.ra_ResponseWindowSize         : raw:7 decoded:sf10  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.ra_SupervisionInfo.mac_ContentionResolutionTimer : raw:5 decoded:sf48  
[RRC]   radioResourceConfigCommon.rach_ConfigCommon.maxHARQ_Msg3Tx : 4  
[RRC]   radioResourceConfigCommon.bcch_Config.modificationPeriodCoeff : raw:0 decoded:n2  
[RRC]   radioResourceConfigCommon.pcch_Config.defaultPagingCycle : raw:2 decoded:rf64  
[RRC]   radioResourceConfigCommon.pcch_Config.nB                 : raw:2 decoded:oneT  
[RRC]   radioResourceConfigCommon.prach_Config.rootSequenceIndex                          : 0  
[RRC]   radioResourceConfigCommon.prach_Config.prach_ConfigInfo.prach_ConfigIndex         : 0  
[RRC]   radioResourceConfigCommon.prach_Config.prach_ConfigInfo.highSpeedFlag             : 0  
[RRC]   radioResourceConfigCommon.prach_Config.prach_ConfigInfo.zeroCorrelationZoneConfig : 1  
[RRC]   radioResourceConfigCommon.prach_Config.prach_ConfigInfo.prach_FreqOffset          : 2  





SIB2 结构说明--解释与 RACH 随机接入相关的字段：  

sib2..prach-Config.rootSequenceIndex 30,  取值范围 0--837，这个是 index，有一张表对应实际的 u

value BCCH-DL-SCH-Message ::=   
    message c1 : systemInformation :   
        criticalExtensions systemInformation-r8 :   
            sib-TypeAndInfo   
              sib2 :   
                  radioResourceConfigCommon   
                    rach-ConfigCommon   
                      preambleInfo   
                        numberOfRA-Preambles n40,  
                        preamblesGroupAConfig   
                          sizeOfRA-PreamblesGroupA n32,  
                          messageSizeGroupA b144,  
                          messagePowerOffsetGroupB dB10  
                       ,
                      powerRampingParameters 
                        powerRampingStep dB2,
                        preambleInitialReceivedTargetPower dBm-104
                       ,
                      ra-SupervisionInfo 
                        preambleTransMax n10,
                        ra-ResponseWindowSize sf5,
                        mac-ContentionResolutionTimer sf32
                       ,
                      maxHARQ-Msg3Tx 3
                     ,
                    bcch-Config 
                      modificationPeriodCoeff n8
                     ,
                    pcch-Config 
                      defaultPagingCycle rf64,
                      nB oneT
                     ,
                    prach-Config 
                      rootSequenceIndex 30,  取值范围 0--837，这个是 index，有一张表对应实际的 u
                      prach-ConfigInfo 
                        prach-ConfigIndex 4,
                        highSpeedFlag FALSE,
                        zeroCorrelationZoneConfig 8,
                        prach-FreqOffset 3
                     ,
                    pdsch-ConfigCommon 
                      referenceSignalPower 11,
                      p-b 1
                     ,
                    pusch-ConfigCommon 
                      pusch-ConfigBasic 
                        n-SB 1,
                        hoppingMode interSubFrame,
                        pusch-HoppingOffset 6,
                        enable64QAM FALSE
                       ,
                      ul-ReferenceSignalsPUSCH 
                        groupHoppingEnabled FALSE,
                        groupAssignmentPUSCH 0,
                        sequenceHoppingEnabled FALSE,
                        cyclicShift 0
                     ,
                    pucch-ConfigCommon 
                      deltaPUCCH-Shift ds2,
                      nRB-CQI 1,
                      nCS-AN 0,
                      n1PUCCH-AN 36
                     ,
                    soundingRS-UL-ConfigCommon release : NULL,
                    uplinkPowerControlCommon 
                      p0-NominalPUSCH -100,
                      alpha al1,
                      p0-NominalPUCCH -100,
                      deltaFList-PUCCH 
                        deltaF-PUCCH-Format1 deltaF0,
                        deltaF-PUCCH-Format1b deltaF1,
                        deltaF-PUCCH-Format2 deltaF0,
                        deltaF-PUCCH-Format2a deltaF0,
                        deltaF-PUCCH-Format2b deltaF0
                       ,
                      deltaPreambleMsg3 1
                     ,
                    ul-CyclicPrefixLength len1
                   ,
                  ue-TimersAndConstants 
                    t300 ms200,
                    t301 ms200,
                    t310 ms500,
                    n310 n10,
                    t311 ms3000,
                    n311 n1
                   ,
                  freqInfo 
                    ul-CarrierFreq 20600,
                    ul-Bandwidth n50,
                    additionalSpectrumEmission 12
                   ,
                  timeAlignmentTimerCommon sf10240
