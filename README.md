# NetWatch

一个跨平台（Windows + Android）的 **WiFi 局域网设备监控工具**。  
用于检测新设备接入 WiFi / 局域网，并即时提醒用户。  
适合家庭网络安全、自用 WiFi 监控、物联网设备发现等场景。

当前已实现：
- Windows 端通过 ARP/DHCP 抓包检测新设备接入  
- Windows 11 Toast 通知  
- DHCP Hostname / Vendor 解析  
- 已知设备自动记录

未来计划（逐步实现）：
- Windows 后台服务版（常驻托盘）  
- Android 客户端版本（本地扫描 + 与 Windows/Server 同步）  
- 设备离线检测  
- 设备备注名、标签、信号强度显示  
- 多设备聚类识别（解决随机 MAC 问题）  
- Web 面板 / 云端同步（可选）

---

## ✨ 功能亮点（当前版本）

### ✔ 实时检测新设备上线  
通过监听局域网内 ARP + DHCP 包，当有新设备加入网络时自动触发事件。

### ✔ Windows 11 Toast 提醒  
在桌面右下角显示流畅的 Win11 风格通知。

### ✔ DHCP Hostname 解析  
自动提取设备的：
- 主机名（Hostname）
- Vendor Class Identifier（部分安卓会带）

### ✔ 已知设备持久化记录  
所有识别过的设备 MAC 会自动写入 `known_macs.json`，避免重复提醒。

---

## 🖥️ Windows 端运行方式（开发者模式）

前置条件：
- Windows 10 / 11
- 已安装 Npcap（Wireshark 可抓包则说明已安装）
- Python 3.8+

安装依赖：

```bash
pip install -r windows/sniff_service/requirements.txt
