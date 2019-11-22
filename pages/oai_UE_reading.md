# main() of **UE**

create_tasks_ue()  
----itti_create_task (TASK_NAS_UE, **nas_ue_task**, users)  
----itti_create_task (TASK_RRC_UE, **rrc_ue_task**, NULL)  
init_UE(NB_UE_INST...)  
----l2_init_ue()  
----init_UE_threads()  
--------create thread **UE_thread_rxn_txnp4**  
--------create thread **UE_thread_synch**  
----create thread **UE_thread**  
pthread_cond_broadcast(&sync_cond)  
printf("TYPE <CTRL-C> TO TERMINATE\n")  
itti_wait_tasks_end()----- waiting forever here
