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

**核心网**代码： 
>$ git clone https://github.com/OPENAIRINTERFACE/openair-cn.git

这两个仓库分别放在两个不同的地方托管，核心网的代码与UE端的代码，用的 LICENSE 不同，所以分开两个仓库管理的。

如果要尝试**5G核心网**，则需要 clone 另外的仓库：
>$ git clone https://github.com/OPENAIRINTERFACE/openair5g-cn.git

# 编译 eNB/UE
## 编译准备
安装需要的软件包
>source ./oaienv  
>sudo ./build_oai -I

## 编译（非仿真情况）
进入 openairinterface5g.git 仓库所在目录
进入到 cmake_targets 子目录下
执行如下命令：
>$ sudo ./build_oai --eNB --UE

## PHY Simulation 编译
>cd cmake_targets
./build_oai --phy_simulators


# 编译核心网工程（非 5G）
## 编译准备
安装需要的软件包
>source ./oaienv    
>sudo ./build_oai -I

# Running
## to run eNB
> enter the directory:   **/openairinterface5g/cmake_targets/lte_build_oai/build**  
> ENODEB=1 sudo -E ./lte-softmodem -O ~/OAI/openairinterface5g/ci-scripts/conf_files/lte-fdd-basic-sim.conf --basicsim  

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
