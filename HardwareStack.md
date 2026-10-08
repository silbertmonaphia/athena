# PicoRV32 BSP 项目 — 工具栈 + 简历总结

> **目的:** 简历可粘贴、面试可背诵、GitHub README 可嵌入。
> **覆盖项目:** PicoRV32 BSP(4 周,W1-W4,见 [Schedule.md](./Schedule.md))。
> **目标岗位:** SoC BSP / Firmware Engineer(芯片公司方向)。

---

## 简历单行总结

> 在 RISC-V 软核 PicoRV32 上完成 BSP 开发(UART/SPI/GPIO 驱动 + Buildroot + Linux 启动到 shell),工具栈涵盖 iverilog/Verilator/Buildroot/QEMU/RISC-V GCC 工具链/OpenOCD。GitHub 公开 + 演示视频。

---

## 工具栈全表

### 硬件 / HDL 工具

| 工具 | 用途 | 何时用 | 优先级 |
|---|---|---|---|
| **iverilog / Icarus Verilog** | Verilog 仿真 | W1 入门 + 全程 | 🔴 最高 |
| **Verilator** | 高性能 Verilog 仿真 | W2-W3 调试 | 🟡 高 |
| **EDA Playground** | 在线仿真(零配置) | W1 跑小项目 | 🟢 中 |
| **GTKWave** | 波形查看 | 调试时 | 🟡 高 |
| **Vivado / Quartus**(可选) | FPGA 综合 | 有板子时 | 🟢 中 |

### 软件 / 系统工具

| 工具 | 用途 | 何时用 | 优先级 |
|---|---|---|---|
| **RISC-V GCC 工具链**(`riscv64-unknown-elf-gcc`) | 交叉编译 | W2-W4 全程 | 🔴 最高 |
| **Buildroot** | 嵌入式 Linux 构建 | W3 里程碑 | 🔴 最高 |
| **Linux Kernel**(`make menuconfig` / `make`) | 内核配置 + 编译 | W3 | 🔴 最高 |
| **QEMU**(`qemu-system-riscv32`) | RISC-V 模拟器 | W3 启动到 shell | 🔴 最高 |
| **u-boot / OpenSBI** | Bootloader | W3 | 🟡 高 |
| **OpenOCD + GDB** | 调试器(在线仿真) | W2 调试 | 🟡 高 |
| **busybox** | 用户空间工具集 | W3 rootfs | 🟢 中 |
| **设备树 (DeviceTree)** | 外设描述 | W2-W3 | 🔴 最高 |

### 调试 / 串口工具

| 工具 | 用途 | 优先级 |
|---|---|---|
| **minicom / picocom** | 串口终端(看 UART 输出) | 🟡 高 |
| **Wireshark** | 网络/总线协议分析(可选) | 🟢 中 |
| **strace / ltrace** | 系统调用追踪(Linux 启动调试) | 🟡 高 |

### 项目协作工具

| 工具 | 用途 |
|---|---|
| **Git + GitHub** | 版本控制 + 简历展示 |
| **Markdown + 中英双语 README** | 项目文档 |
| **OBS Studio + ffmpeg** | 演示视频录制剪辑 |
| **Docker**(可选) | Buildroot 容器化环境 |

---

## 概念栈(简历可写)

### 协议层

- **RISC-V ISA**(RV32IMC + Zicsr)
- **Wishbone 总线**(standard / pipelined)
- **AMBA AXI4-Lite**(可加分,大厂面试常见)
- **PLIC / CLINT**(中断控制器)

### 系统层

- **MMIO**(内存映射 I/O)
- **设备树**(DTS / DTB)
- **Boot sequence**(BootROM → OpenSBI → u-boot → Linux)
- **Linker script**
- **交叉编译**

### CPU 概念

- **5 级流水线**
- **Cache + MESI 一致性**
- **CSR**(控制状态寄存器)
- **Trap 处理**

---

## 简历写法模板(STAR)

```
项目:PicoRV32 SoC 软件移植(GitHub:xxx)

(S) 背景:从量化研究转型芯片方向,需快速建立 SoC 软件栈实战经验。
(T) 目标:在 RISC-V 软核 CPU 上完成完整 BSP(Board Support Package),
       启动到 Linux shell。
(A) 行动:
  - 基于 YosysHQ PicoRV32 软核 CPU,完成 UART/SPI/GPIO 驱动开发
  - 集成 Buildroot,定制 Linux 内核 + 根文件系统
  - 用 QEMU 模拟器完成启动验证(BootROM → OpenSBI → u-boot → Linux → shell)
  - 工具链:iverilog / Verilator / QEMU / RISC-V GCC / Buildroot / OpenOCD
(R) 结果:
  - 项目 4 周完成,GitHub star X,演示视频在 B 站 / YouTube
  - 覆盖 SoC 软件栈核心技能:BSP 驱动 + Linux 移植 + 工具链
```

---

## 面试自我介绍(90 秒版)

> "过去 4 周我自建了 PicoRV32 BSP 项目,基于 RISC-V 开源软核 CPU 完成了 UART/SPI/GPIO 三个外设驱动开发,集成 Buildroot 把 Linux 移植上去,启动到 shell。整个工具栈跟商业芯片公司的 BSP 工程师日常完全一样——iverilog 仿真、QEMU 启动验证、RISC-V GCC 交叉编译、Buildroot 构建、OpenOCD 调试。我之前有 5 年互联网后端经验,工程能力强,数学和算法基础扎实,所以转 SoC 软件栈主要是补硬件和驱动这块——4 周这个项目就是补这块的证明。"

---

## 为什么这个 stack 对芯片公司值钱

- ✅ **80% 工具是 SoC 软件栈通用**——任何芯片公司面试都认
- ✅ **RISC-V 是当下热点**——平头哥 / SiFive / 兆易都在做
- ✅ **Linux 启动到 shell**——BSP 工程师核心能力证明
- ❌ **不带 AI 算法**——别在简历里硬蹭 AI(详见 [Schedule.md §投递筛选标准](./Schedule.md))

---

## 相关文档

- [Schedule.md](./Schedule.md) — 战术执行表(每天 10h 怎么分,4 周怎么走,W4 末测试投 + W5 正式投)
- [CAREER.md](./CAREER.md) — 战略规划(为什么转型,4 个月见 offer 的整体策略)
- [DataStructure_Alg.md](./DataStructure_Alg.md) — 103 题 + 💎 双倍收益标注
