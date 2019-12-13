# RACH generating
## 总体步骤描述
UE 向 eNB 发送随机接入信号，在 64 个 “**随机接入序列**” 中**随机**选择一个。  
64 个 “**随机接入序列**” 的生成过程：  
1）用基本的 Zaddoff-Chu 公式，生成一个 基序列(base sequence)  
2）根据基序列生成 64 个“**随机接入序列**”: 用 cyclic shift 的方法，即用64个 移位步长（可能有相同的 0 shift，即不 shift）对基序列做 cyclic shift.

## 生成 zaddoff chu 序列(基序列)
### 公式
Generate a Zaddoff Chu sequence (839 or 139 samples) using rootSequenceIndex (let's call this sequence as 'base sequence')  

![prach_zaddoff_chu_formula](http://taichiorange.github.io/images/lte_initial_attach/36_211_Zadoff_RACH.PNG)

Nzc indicate 'number of data in the ZaddOff Chu Sequence'. This number is fixed to be **839** in preamble format 0, 1,2,3 and **139** in preamble format 4, notes: format 4 is used only in TDD LTE. Refer to  table <36.211-Table 5.7.2-1: Random access preamble sequence length>  
Format 0,1,2,3,4是由基站决定的。见下一节 **format**
### format 的决定
eNB 通过 SIB2 字段 prach-Configindex 来间接决定 format 的，参考下表：
![prach_configIndex](http://taichiorange.github.io/images/lte_initial_attach/LTE_PRACH_ConfigIndex_PreambleFormat_01.png)  

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
![prach_Ncs](http://taichiorange.github.io/images/lte_initial_attach/PRACH_Ncs.PNG)


### 对于 unrestricted sets 情况
根据 Nzc 和 Ncs 就可以计算出来 Cv.    
> Ncs = 0 : Cv = 0  
> Ncs != 0: Cv = v 乘以 Cv, 其中， v 取值按照上图范围来取。  
？？？ 这里能保证得到 64 个 Cv 吗？  

### restricted sets 情况
这个情况复杂很多，需要知道如下四个数据：




# SIB2 结构说明--解释与 RACH 随机接入相关的字段 

sib2..prach-Config.rootSequenceIndex 30,  取值范围 0--837，这个是 index，有一张表对应实际的 u  


![prach_SIB2_parameters](http://taichiorange.github.io/images/lte_initial_attach/RACH_SIB2_Parameters.png)

