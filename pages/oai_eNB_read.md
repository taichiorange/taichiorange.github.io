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












![fftshift](http://taichiorange.github.io/images/fftshift/CableFree-S1-lte-interface.gif)
