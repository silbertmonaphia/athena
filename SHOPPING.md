# PicoRV32 BSP 项目硬件采购指南 — W4 末决策树

> **目的:** 回答一个问题 — **"4 周 PicoRV32 BSP 项目需要买硬件吗?买什么?多少钱?"**
>
> **生成日期:** 2026-10。**版本:** v1.0。**下次回顾:** 2026-11(W3 末决策点)
>
> **核心结论先放:** **$0 起步,QEMU 完整覆盖 4 周计划。W3 末如果觉得 QEMU 演示不够"实",再加 ¥80-150 买国产 Sipeed Tang Nano 9K FPGA 板做真实硬件 blinky。** 不买 RV64 板(¥1500+ 不对口)。

---

## 一、QEMU 路线真的够吗?— 数据验证

| 验证项 | 数据 | 来源 |
|---|---|---|
| QEMU 官方支持 RISC-V | ✅ `qemu-system-riscv32` 官方二进制 | QEMU Wiki |
| Buildroot 提供现成配置 | ✅ `make qemu_riscv32_virt_defconfig` 一键构建 | Buildroot 官方 |
| 启动到 shell 是常规路径 | ✅ OpenSBI + Image + rootfs.ext2 + virtio-blk | 多个 RISC-V BSP 教程 |
| OpenSBI 跑在 QEMU | ✅ `fw_jump.elf` 直接加载 | QEMU upstream docs |
| PicoRV32(软核)做 RTL 仿真 | ✅ iverilog / Verilator 跑 Hello World | YosysHQ PicoRV32 demo |

**结论:** 你的 W3 里程碑"PicoRV32 启动到 Linux shell"在 QEMU 里**就是一行命令的事**。硬件不是必要条件。

---

## 二、三个预算档位对比

### 2.1 Tier 0:$0(默认推荐,够用)

| 工具 | 替代什么硬件 | 完成什么里程碑 |
|---|---|---|
| **QEMU `qemu-system-riscv32 -M virt`** | 真实 RISC-V 开发板 | W3 启动到 Linux shell ✅ |
| **iverilog / Verilator** | FPGA 板 | W1 PicoRV32 RTL 仿真 ✅ |
| **Buildroot `qemu_riscv32_virt_defconfig`** | 交叉编译 + rootfs | W3 Buildroot 集成 ✅ |
| **OpenSBI + busybox/busybear** | bootloader | W3 ✅ |
| **screen / OBS** | 录演示视频 | W4 ✅ |

**演示视频(QEMU 路线)可以这样拍:**
- QEMU 终端窗口(PicoRV32 跑 Linux 进 shell)
- GTKWave 波形(PicoRV32 RTL 仿真,UART 输出)
- VSCode 截图(设备树 + 驱动代码 + GitHub commit 历史)

**完全够 4 周项目交付。**

---

### 2.2 Tier 1:¥80-300(可选,加分项)

| 板子 | 价格 | 用途 | 适配度 |
|---|---|---|---|
| **Sipeed Tang Nano 9K / Primer 25K** | ¥80-150(GW1NR-9 / GW5A) | FPGA 跑 PicoRV32 软核,**真实 LED 闪烁** | ⭐⭐⭐⭐⭐ |
| **Lattice iCEBreaker** | $100-150(¥700-1000) | 国外 FPGA,自带 USB + LEDs | ⭐⭐⭐(海淘慢) |
| **Sipeed Longan GD32V** | ¥30-50 | RISC-V MCU,可跑 RTOS | ⭐⭐(不是 Linux) |
| **CH32V103 / W806** | ¥10-20 | 入门级 RISC-V MCU | ⭐(太低端,意义不大) |

**性价比最高:** **Sipeed Tang Nano 9K**(¥80-150,国产现货,嘉立创/立创商城发货快)

**W4 演示视频可以这样拍:**
- 实物 LED 闪烁 + UART 串口输出"PicoRV32 BSP ready"
- 比 QEMU 截图更有视觉冲击
- 演示视频 B 站播放量大概率翻倍

---

### 2.3 Tier 2:¥1500+(不推荐现阶段买)

| 板子 | 价格 | 问题 |
|---|---|---|
| **LicheePi 4A**(全志 TH1520) | ¥1500-2000 | **64-bit,跟你 PicoRV32 RV32 不对口** |
| **VisionFive 2**(StarFive JH7110) | ¥2000+ | 64-bit,不对口 |
| **Sipeed Nezha**(全志 D1) | ¥300-400 | 64-bit,不对口 |

**问题:** 这些是 **RV64** Linux 板,**跟你的 PicoRV32 RV32 项目不对口**。等你拿到 offer 进了芯片公司再买不迟。

---

### 2.4 Tier 3:¥300-500(过度配置,跳过)

JTAG 调试器 + 逻辑分析仪 + 示波器。这是**已经在芯片公司上班的人**的配置。你现在不需要。

---

## 三、我的具体建议(基于你的 4 个月 runway)

### 3.1 W1-W3:$0 完全够用

```
W1: iverilog/EDA Playground + PicoRV32 RTL 仿真(0 元)
W2: Verilator + Verilog 驱动开发(0 元)
W3: QEMU + Buildroot + Linux 启动到 shell(0 元)
```

**演示视频用 screen / OBS 录屏,完全够用。**

### 3.2 W3 末决策点:加不加 Tier 1?

```
做完 W3 后问自己:QEMU 演示够有说服力吗?
├─ ✅ 看起来够 → 不买硬件,$0
└─ ❌ 差点意思 → 加 ¥80-150 买 Sipeed Tang Nano 9K
                └─ 加做 W4 的"FPGA 真实硬件 blinky"演示
```

### 3.3 不买 Tier 2-3

**理由:**
- RV64 板跟 PicoRV32 RV32 不对口
- ¥1500-2000 占你 4 个月 runway 的 5-7%(**不算小**)
- 进了芯片公司公司会配

---

## 四、WSL2 特别提示(你的环境是 WSL2)

**关键事实:** WSL2 默认**不能直接访问 USB 设备**。

### 4.1 三种 USB 透传方案对比

| 方案 | 配置复杂度 | 稳定性 | 推荐场景 |
|---|---|---|---|
| **A. usbipd-win + usbip(WSL2)** | 🟡 中 | 🟡 中(偶发断连) | 临时调试 |
| **B. VirtualBox/VMware Linux 虚拟机** | 🟢 低 | 🟢 高(原生 USB) | **Tier 1 长期使用** |
| **C. Windows 工具 + WSL2 编译** | 🟢 低 | 🟢 高 | **最简单方案** |

### 4.2 推荐做法

**如果你只买 Tier 1 一块板子,临时调试:**
- 方案 C:**板子插 Windows,串口/JTAG 用 Windows 工具**(PuTTY / OpenOCD for Windows),**WSL2 里跑仿真和编译**
- 这是阻力最小的路径

**如果你打算长期接板子调试:**
- 方案 B:装个 VirtualBox/VMware Linux 虚拟机,把板子 USB 透传到虚拟机里
- WSL2 跑仿真/编译,虚拟机跑硬件调试

**如果你只用 Tier 0(QEMU 路线):**
- **完全不用管 USB 透传。** QEMU 纯软件,USB 啥事没有。

---

## 五、采购决策树(W3 末执行)

```
W3 末(2026-11-05 左右)坐下来,按这个走:
│
├─ Q: PicoRV32 在 QEMU 启动到 Linux shell 跑通了吗?
│  ├─ ❌ 没跑通 → 不买硬件,先把 QEMU 跑通(这是核心)
│  └─ ✅ 跑通了 → 继续
│
├─ Q: QEMU 演示视频看起来有说服力吗?
│  ├─ ✅ 够 → 不买硬件,直接 W4 准备投递($0)
│  └─ ❌ 差点意思 → 继续
│
├─ Q: 愿意花 ¥80-150 让 W4 演示视频更有冲击?
│  ├─ ❌ 不愿意 → 不买,用现有素材
│  └─ ✅ 愿意 → 继续
│
└─ Q: 选哪块?
   ├─ 🟢 Sipeed Tang Nano 9K(¥80-150,国产现货,推荐)
   ├─ 🟡 Sipeed Tang Primer 25K(¥150-200,资源更足)
   └─ 🔴 Lattice iCEBreaker($100-150,海淘 2-3 周,不推荐)
```

---

## 六、不买的清单(避免踩坑)

| 类别 | 不买原因 |
|---|---|
| ❌ RV64 开发板(LicheePi 4A / VisionFive 2 / Nezha) | 跟 PicoRV32 RV32 不对口 |
| ❌ 千元级 FPGA(Vivado / Quartus 板) | 工具链复杂,4 周来不及 |
| ❌ 示波器 / 逻辑分析仪 | 现在用不上 |
| ❌ JTAG 调试器 | QEMU 路线不需要 |
| ❌ 任何"AI 芯片开发板" | 你的项目是 BSP 不是 AI,跑偏 |
| ❌ 万用表 / 电烙铁 / 各种 DIY 工具 | 仿真路线不用 |

---

## 七、如果决定买 Tier 1:具体下单清单

**Sipeed Tang Nano 9K(¥80-150):**
- [ ] 嘉立创商城 / 立创商城 / 淘宝"小梅哥电子"搜"Tang Nano 9K"
- [ ] 默认配置即可(无需屏幕 / 外壳)
- [ ] USB Type-C 线(用你充电线就行)
- [ ] **不需要**:JTAG 调试器(QEMU 路线后续补充)

**额外预算(可选):**
- ¥20-30 Micro-USB 转 UART 模块(CH340 芯片)— 用于接 UART 串口
- 或者直接用板载 USB 转 UART(部分型号自带)

---

## 八、对 4 个月 runway 的财务影响

| 选项 | 支出 | 占 runway 比例(假设 12 万) |
|---|---|---|
| Tier 0($0) | ¥0 | 0% |
| Tier 1(Tang Nano 9K) | ¥150 | 0.1%(可忽略) |
| Tier 1 + 串口模块 | ¥200 | 0.2%(可忽略) |
| Tier 2(若误买 RV64 板) | ¥1500+ | 1.3%+(**不小**) |

**结论:** Tier 0 和 Tier 1 对 runway 几乎没影响;**Tier 2 才是真正的财务负担,坚决不买。**

---

## 九、相关文档

- [`HardwareStack.md`](./HardwareStack.md) — 工具栈总表(本文件是它的"硬件采购"补充)
- [`Trend.md`](./Trend.md) §1.4 — AI 时代 BSP 工作流(真硬件调试会用到 §1.4 的 L3 能力)
- [`Schedule.md`](./Schedule.md) — W1-W4 时间表 + AI 工程化工作流约束
- [`CAREER.md`](./CAREER.md) — 4 个月 runway 财务背景

---

## Sources

- [QEMU Wiki:RISC-V Platform](https://wiki.qemu.org/Documentation/Platforms/RISCV)
- [QEMU Upstream:RISC-V System emulator](https://qemu.org/docs/master/system/target-riscv.html)
- [Luca Berton:Getting Started with RISC-V on QEMU(2026)](https://lucaberton.com/blog/getting-started-risc-v-qemu-emulation-linux/)
- [Sipeed LicheePi 4A RISC-V Linux SBC](https://elemart.com/shop/product/1687/sipeed-licheepi-4a-risc-v-th1520-linux-sbc-development-board)
- [Sipeed Tang Nano 9K 资料(Gowin FPGA)](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-9K/intro.html)
- [Buildroot:qemu_riscv32_virt_defconfig](https://buildroot.org/)

---

**单一铁律:** **W3 末做决策,不提前买。QEMU 跑通之前不要碰硬件。** 真要买只买 Sipeed Tang Nano 9K(¥80-150),其他全不买。
