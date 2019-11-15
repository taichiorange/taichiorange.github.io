# to create tasks of eNB
## init_eNB_proc()  
   init_te_thread: create **te_thread** in which deal with dlsch    
   init_td_thread: create **td_thread** in which deal with ulsch    

## int create_tasks(uint32_t enb_nb)
### MUST
TASK_ENB_APP, eNB_app_task  
TASK_RRC_ENB, rrc_enb_task  
### Optional, but created
TASK_SCTP, sctp_eNB_task  
TASK_S1AP, s1ap_eNB_task  
TASK_UDP, udp_eNB_task: this is for emulated RF  
TASK_GTPV1_U, gtpv1u_eNB_task

### Optional, but **NOT** created:  
> TASK_X2AP, x2ap_task  
> TASK_CU_F1, F1AP_CU_task  
> TASK_DU_F1, F1AP_DU_task





# LTE architecture

Control Plane Protocol
> S1-AP  ------------ 无线网络层  
> SCTP  
> IP
> Shuju Lianlu Ceng  
> Wuli Ceng

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

The LTE S1-MME interface is responsible for delivering signaling protocols between the eNodeB and the MME. S1-MME interface consists of a Stream Control Transmission Protocol (SCTP) over IP and supports multiple UEs through a single SCTP association. It also provides guaranteed data delivery. The application signaling protocol is an S1-AP (Application Protocol). The LTE S1-MME is responsible for Evolved Packet System (EPS) bearer setup/release procedures, the handover signaling procedure, the paging procedure and the NAS transport procedure.

![S1](http://taichiorange.github.io/images/lte_arch/CableFree-S1-lte-interface.gif)

# 5G DU and CU
![5G](http://taichiorange.github.io/images/5G/5G_arch_E1F1-1.png)
