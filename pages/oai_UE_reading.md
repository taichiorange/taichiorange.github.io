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

# UE_thread() 线程

trx_read_func, 这是一个函数指针，指向了 tcp_bridge_write  
trx_write_func,这是一个函数指针，指向了 tcp_bridge_read  

# UE_thread_rxn_txnp4  
phy_procedures_UE_RX  
ue_scheduler  
----rrc_rx_tx_ue()  
-------- check whether T300 timeout: whether RRC connect failed/timeout  
phy_procedures_UE_TX()  
----ue_prach_procedures()  
--------ue_get_rach(): get resource(such as RA windown) from upper layers  
--------get_tx_amp()  
--------generate_prach()  
--------Msg1_transmitted():这里不是真正传数据的地方，传数据在 UE_thread() 中的 trx_write_func 那里。  
  
