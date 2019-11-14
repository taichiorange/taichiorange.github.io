# to create tasks of eNB
int create_tasks(uint32_t enb_nb)
## MUST
TASK_ENB_APP, eNB_app_task  
TASK_RRC_ENB, rrc_enb_task  
## Optional, but created
TASK_SCTP, sctp_eNB_task  
TASK_S1AP, s1ap_eNB_task  
TASK_UDP, udp_eNB_task: this is for emulated RF  
TASK_GTPV1_U, gtpv1u_eNB_task

## Optional, but **NOT** created:  
> TASK_X2AP, x2ap_task  
> TASK_CU_F1, F1AP_CU_task  
> TASK_DU_F1, F1AP_DU_task









# SCTP

SCTP refers to the Stream Control Transmission Protocol
LTE S1-MME (control plane)

The LTE S1-MME interface is responsible for delivering signaling protocols between the eNodeB and the MME. S1-MME interface consists of a Stream Control Transmission Protocol (SCTP) over IP and supports multiple UEs through a single SCTP association. It also provides guaranteed data delivery. The application signaling protocol is an S1-AP (Application Protocol). The LTE S1-MME is responsible for Evolved Packet System (EPS) bearer setup/release procedures, the handover signaling procedure, the paging procedure and the NAS transport procedure.

![fftshift](http://taichiorange.github.io/images/fftshift/CableFree-S1-lte-interface.gif)
