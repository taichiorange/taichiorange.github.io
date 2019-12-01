# to create tasks of eNB
## init_eNB_proc()  
   init_te_thread: create **te_thread** in which deal with dlsch(downlink)    
   init_td_thread: create **td_thread** in which deal with ulsch(uplink)  
   **eNB_thread_prach**  
   **eNB_thread_prach_br**  
## init_RU_proc()
**ru_thread**  

## int create_tasks(uint32_t enb_nb)
### MUST
TASK_ENB_APP, eNB_app_task  
TASK_RRC_ENB, rrc_enb_task  
### Optional, but created
TASK_SCTP, sctp_eNB_task  
TASK_S1AP, s1ap_eNB_task  
TASK_UDP, udp_eNB_task ？？  
TASK_GTPV1_U, gtpv1u_eNB_task

### Optional, but **NOT** created:  
> TASK_X2AP, x2ap_task  
> TASK_CU_F1, F1AP_CU_task  
> TASK_DU_F1, F1AP_DU_task

# eNB 收发数据

由线程 **ru_thread()** 负责读取和发送数据，分别调用下面两个函数指针：  
( 在没有创建 ru_thread_tx 线程的情况下）  
1）ru->fh_south_in  
2）ru->fh_south_out  

**rxtx()** 函数负责数据处理（eNB 接收）和生成 (eNB 发送）

## eNB tx

----------- data tx --------begin-------------------------------------  
**txs = ru->rfdevice.trx_write_func** is pointed to **tcp_bridge_write()**  
**u->rfdevice.trx_write_func** is called by **tx_rf()**  
**ru->fh_south_out** is pointed to **tx_rf()**  
**ru->fh_south_out** is called by **ru_thread()**  
----------- data tx -------- end -------------------------------------  
----------- wakeup 1ms --------begin-------------------------------------  
**phy_procedures_eNB_TX()** is called by **rxtx()**.  
**rxtx()** is called by **eNB_top()**.  
**eNB_top** is pointed to ***RC.ru[ru_id]->eNB_top*** in the function **init_eNB_afterRU()**  [1]  
***RC.ru[ru_id]->eNB_top*** is called in **wakeup_L1s()**  
**wakeup_L1s()** is called in the loop of **ru_thread**  
**ru_thread** is **CREATED** by **init_RU_proc()**  
**init_RU_proc()** is called by **init_RU**      (notes: Radio Remote Unit(RRU) )  
**init_RU()** is called by **main()** in the eNB project **lte-softmodem.c** **!**  
 ----------- wakeup 1ms --------end-------------------------------------  
 
 [1] **init_eNB_afterRU()**  is called by **main()** in the eNB project **lte-softmodem.c** **!** 

  notes: **wakeup_L1s()** is called each ms ( subframe )  

## eNB rx
----------- data rx --------begin-------------------------------------  
**trx_read_func** is pointed to **tcp_bridge_read()** when using TCP bridge.  
**UE** uses **tcp_bridge_read()** and **tcp_bridge_read_ue** both **!**  
**rxs = ru->rfdevice.trx_read_func()** is called when need to read data in. This is called by **rx_rf()**.  
**rx_rf()** is assigned to a function pointer: **fh_south_in**  
**fh_south_in** is called **ru_thread()**, **ru_thread()** 每读进来一个 subframe，就认为 1ms 时间到了.  
*Notes: ru_thread 的核心内层循环，“it loops over subframes which are scheduled by **incoming** samples from HW devices”*  
----------- data rx -------- end -------------------------------------  

------rx data processing-----begin-------------------------------------  
**phy_procedures_eNB_uespec_RX()** is called in **rxtx()**    
------rx data processing-----end-------------------------------------  

# eNB_thread_prach thread  
--prach_procedures()  
----rx_prach()  
------rx_prach0()  
---------- calculate **max_preamble_energy** and **avg_preamble_energy**  



# rxtx() function
wakeup_prach_eNB()  
wakeup_prach_eNB_br()  

# RACH flow
rxtx()  
----UL_indication()  
--------handle_rach()  
------------initiate_ra_proc()---handles the event of MSG1 reception, **ra[i].state = MSG2**  
--------eNB_dlsch_ulsch_scheduler()  
------------schedule_RA()  
----------------generate_Msg2() when **"if (ra->state == MSG2)"**  
----------------generate_Msg4  
----------------check_Msg4_retransmission()  


