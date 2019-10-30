# 我的命令行工具
## 安装

```bash
pip install git+https://github.com/hezhefly/pycmd.git
```

## `fpip`使用方法

> 我们都知道，pip命令在国内使用，需要镜像站进行加速，虽然可以通过配置文件(参考我的博文)进行永久配置，但一旦变更环境还需要重新进行繁琐的配置工作。
> 综合上面的技术，我们可以通过自定义系统命令，将加速的镜像源地址写入程序，以达到加速的目的。

- 标准安装： `fpip install torch` 
- 升级安装： `fpip install torch --u` 
- github安装： `fpip install https://github.com/pypa/pip.git` 
- github升级安装： `fpip install https://github.com/pypa/pip.git --u` 