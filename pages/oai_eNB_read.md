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
