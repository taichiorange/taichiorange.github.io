**OpenAirInterface安装记录**

# 软件环境
>$   lsb_release -a  
>No LSB modules are available.  
>Distributor ID:	Ubuntu  
>Description:	Ubuntu 18.04.3 LTS  
>Release:	18.04  
>Codename:	bionic  



#  clone 下载源码
**UE/eNB**端的代码：
>$ git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git

# 编译 eNB/UE
## 编译准备
安装需要的软件包
>source ./oaienv  
>sudo ./build_oai -I
### ASN1c install
In this file 
> OAI/openairinterface5g/cmake_targets/tools/build_helper  

the ASN1c is git cloned and installed: 
>git clone https://gitlab.eurecom.fr/oai/asn1c.git /tmp/asn1c  

but CLONE is very slow and easy to abort, we can git clone it before "build_oai -I"  
then copy the repo to /tmp/asn1c

## 编译（非仿真情况）
进入 openairinterface5g.git 仓库所在目录
进入到 cmake_targets 子目录下
执行如下命令：
>$ sudo ./build_oai --eNB --UE

If you want to compile **UE** after modifying some codes ( do not comiple LIBs):
> enter the directory:   **/openairinterface5g/cmake_targets/lte_build_oai/build**  
> sudo make lte-uesoftmodem

If you want to **eNB** after modifying some codes ( do not comiple LIBs):
> enter the directory:   **/openairinterface5g/cmake_targets/lte_build_oai/build**  
> sudo make lte-softmodem

## PHY Simulation 编译
>cd cmake_targets
./build_oai --phy_simulators

## compile tcp_bridge_oai

When simulating RF by using TCP, this file is used:
>targets/ARCH/tcp_bridge/tcp_bridge_oai.c  

build the tcp_bridge only:
> cd /openairinterface5g/cmake_targets/lte_build_oai/build  
> sudo make tcp_bridge_oai  

This is a **.so** file, dynamically used, so do not need to re-compile **lte-uesoftmodem** and **lte-softmodem** 

# Running
## to run eNB
> enter the directory:   **/openairinterface5g/cmake_targets/lte_build_oai/build**  
> ENODEB=1 sudo -E ./lte-softmodem -O ~/OAI/openairinterface5g/ci-scripts/conf_files/lte-fdd-basic-sim.conf --basicsim  

If you do not debug NB-IoT, should use this command:  
>ENODEB=1 sudo -E ./lte-softmodem -O ~/OAI/openairinterface5g/ci-scripts/conf_files/lte-fdd-basic-sim.conf --basicsim --**nbiot-disable** | sudo tee enb_debug.log  
(otherwise, error message : "[LOADER] library libNB_IoT.so is not loaded: libNB_IoT.so: **cannot** open shared object file: No such file or directory"  
  
or  
> ENODEB=1 sudo -E ./lte-softmodem -O ~/OAI/openairinterface5g/ci-scripts/conf_files/lte-fdd-basic-sim.conf --basicsim --noS1  

## to run UE
### generate config file
>  edit  vim ~/OAI/openairinterface5g/openair3/NAS/TOOLS/ue_eurecom_test_sfr.conf  
>  enter the directory:   **/openairinterface5g/cmake_targets/lte_build_oai/build**  
>  sudo ../../nas_sim_tools/build/conf2uedata -c ~/OAI/openairinterface5g/openair3/NAS/TOOLS/ue_eurecom_test_sfr.conf -o ./
### to run
> enter the directory:   **/openairinterface5g/cmake_targets/lte_build_oai/build**   
> sudo -E ./lte-uesoftmodem -C 2625000000 -r 25 --ue-rxgain 140 --basicsim
# 碰到问题
## 443 问题
>正克隆到 '/opt/ssh'...  
>fatal: unable to access 'https://gist.github.com/2190472.git/': Failed to connect to gist.github.com port 443: 连接超时

则用vim打开 build_helper文件，即 vim tools/build_helper  注释下面两行代码

   >$SUDO rm -fr /opt/ssh  
   >$SUDO git clone https://gist.github.com/2190472.git /opt/ssh

   原因是 gist.github.com 被**墙**了


## ctags 问题

OAI 提供了一个 脚本，来生成 tags 文件，其中使用了一个参数  -E，会导致生成的 tags文件，在 ubuntu/INTEL 体系下工作不正常（是因为tags文件中生成了一些不可见字符）。

>ctags ***-e*** -R  --exclude=openair1/DOCS/ --exclude=openair2/DOCS/ --exclude=openair2/RRC/CELLULAR/ --exclude=openair2/NAS/DRIVER/CELLULAR/ --exclude=openair2/SIMULATION/ --exclude=targets/DOCS/ --exclude=targets/PROJECTS/ openair1 openair2 openair3 targets cmake_targets common

看 ctags 的帮助文件
> -e   Output tag file for use with Emacs.

所以，要删除 -e 这个选项。

# --noS1 option problem

UE MUST NOT use --noS1 option, otherwise This will result in *PLMN not matching*.
>Synched with a cell, but PLMN doesn't match our SIM


============================================= EPC part =========================================
# **核心网**代码： 
>$ git clone https://github.com/OPENAIRINTERFACE/openair-cn.git

这两个仓库分别放在两个不同的地方托管，核心网的代码与UE端的代码，用的 LICENSE 不同，所以分开两个仓库管理的。

如果要尝试**5G核心网**，则需要 clone 另外的仓库：
>$ git clone https://github.com/OPENAIRINTERFACE/openair5g-cn.git


# 编译核心网工程（非 5G）
## HSS
> cd openair-cn  
> source oaienv  
> cd scripts  
> ./build_hss -i  
> ./build_hss

## MME
> ./build_mme -i  
>   

