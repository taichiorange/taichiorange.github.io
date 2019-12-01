<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
# LTE Architecture
![lte-archtecture](http://taichiorange.github.io/images/lte_arch/LTE-network-architecture.png)

# NPRACH
format 0: 1.4ms = 67us + 1.333ms = 1.4ms  
format 1: 1.6ms = 267us+ 1.333ms = 1.6ms  
其中 Ts = $$\frac{1}{30.72M}=32.55ns$$

![nprach](http://taichiorange.github.io/images/nb_iot/LTE_NB_RACH_TimeFrequencyStructure_01.png)

# NB-IoT 随机接入过程图
![nbiot_rach_flow](http://taichiorange.github.io/images/nb_iot/LTE_NB_RACH_InitialAttach_01.png)

# LTE RACH
## when and where does UE send RACH?
PRACH Configuration Index is determined by SIB2 parameter **prach-ConfigIndex**.  
PRACH Configuration Index determines when and where UE sends RACH.  
![prach_ConfigIndex](http://taichiorange.github.io/images/lte_initial_attach/RACH_Configuration_Index.png)



## LTE RACH 流程图（含 RAR response window 图）
### RACH 流程图  
![lte_rach_flow1](http://taichiorange.github.io/images/lte_initial_attach/FullRACH_Sample01.png)
![lte_rach_flow2](http://taichiorange.github.io/images/lte_initial_attach/FullRACH_Sample02.png)  
### RAR( RACH Response) 流程及其窗口示意图
![lte_rach_flow2](http://taichiorange.github.io/images/lte_initial_attach/RAR_response_window.png)  


# LTE architecture

Control Plane Protocol
> S1-AP  ------------ 无线网络层  
> SCTP  
> IP  
> 数据链路层  
> 物理层

![control plan](http://taichiorange.github.io/images/lte_arch/control_plan.png)

User Plane Protocol
> GTP-U  
> UDP  
> IPv6 or IPv4  
> 数据链路层  
> 物理层

![control plan](http://taichiorange.github.io/images/lte_arch/user_plan.png)

# SCTP

SCTP refers to the Stream Control Transmission Protocol
LTE S1-MME (control plane)
可以类比为 TCP 协议，在 IP 层之上构建了一个稳定可靠、面向连接的传输层。

The LTE S1-MME interface is responsible for delivering signaling protocols between the eNodeB and the MME. S1-MME interface consists of a Stream Control Transmission Protocol (SCTP) over IP and supports multiple UEs through a single SCTP association. It also provides guaranteed data delivery. The application signaling protocol is an S1-AP (Application Protocol). The LTE S1-MME is responsible for Evolved Packet System (EPS) bearer setup/release procedures, the handover signaling procedure, the paging procedure and the NAS transport procedure.

![S1](http://taichiorange.github.io/images/lte_arch/CableFree-S1-lte-interface.gif)

# 5G DU and CU
![5G](http://taichiorange.github.io/images/5G/5G_arch_E1F1-1.png)

# LTE RACH
Exactly when and Where a UE transmit RACH ?

 

To answer to this question, you need to refer to 3GPP specification TS36.211 - Table 5.7.1-2. This table would give you at which frame and subframe that UE is allowed to transmit a PRACH Preamble. As you see at this table, the prach preamble timing and prach preamble type is determined by PRACH Configuration Index. The, how PRACH Configuration Index is determined ? It is determined by **SIB2** parameter **prach-ConfigIndex**.

 

< TS36.211 - Table 5.7.1-2 : PRACH Configuration Index>
![S1](http://taichiorange.github.io/images/lte_arch/rach_when_where_36_211_Table_5_7_1_2_PRACH.png)


 

Did you open the specification now ? It shows exactly when a UE is supposed to send RACH depending on a parameter called "PRACH Configuration Index".

 

For example, if the UE is using "PRACH Configuration Idex 0", it should transmit the RACH only in EVEN number SFN(System Frame Number). Is this good enough answer ? Does this mean that this UE can transmit the RACH in any time within the specified the SFN ? The answer to this question is in "Sub Frame Number" colulmn of the table. It says "1" for "PRACH Configuration Idex 0". It means the UE is allowed to transmit RACH only at sub frame number 1 of every even SFN.

# eNB 功能划分

**RC**C: **Radio-Cloud** Center  
**RA**U: **Radio-Access** Unit  
R**RU**: Radio **Remote-Unit**  
![control plan](http://taichiorange.github.io/images/openairinterface/eNB_Functional_Splits.png)

# 缩写和名词解释
C-RAN: Centralized RAN
NGFI:  Next Generation Fronthaul Interface
