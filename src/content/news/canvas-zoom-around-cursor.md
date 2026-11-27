---
category: "coding"
summaryEn: "Use the camera’s coordinate transforms to keep the map point under the cursor fixed as the scale changes. A numerical check makes the expected behavior easy to verify."
summaryZh: "利用相机的坐标变换，让缩放前后光标指向同一个地图点，并用一组数字核对结果。"
tags: ["javascript", "canvas", "coordinate-transforms"]
titleEn: "Zoom a Canvas map around the cursor"
titleZh: "让 Canvas 地图以光标为中心缩放"
blocks: [{"code": "function zoomAt(camera, screenX, screenY, nextScale) {\n  const worldX = camera.x + screenX / camera.scale;\n  const worldY = camera.y + screenY / camera.scale;\n\n  camera.scale = nextScale;\n  camera.x = worldX - screenX / nextScale;\n  camera.y = worldY - screenY / nextScale;\n}", "file": "", "kind": "code", "language": "javascript", "title": {"en": "Keep the world point under the cursor fixed", "zh": "固定光标下方的世界坐标"}}]
type: "tutorials"
version: "Canvas 2D camera model documented on 2026-11-26"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T10:02:34+08:00"
sources: [{"title": "Pan and Zoom on a Canvas Map With Pointer Events (Zooming Around the Cursor)", "url": "https://dev.to/seed_map_0edb4c28effd76e5/pan-and-zoom-on-a-canvas-map-with-pointer-events-zooming-around-the-cursor-4c3e"}]
---
<p lang="zh-CN">在 Canvas 地图里，把鼠标移到一个标记上再缩放，标记应该留在光标下方。Seed Map 的示例将相机偏移存为世界坐标，并单独保存缩放比例。绘制时，先从世界坐标减去相机偏移，再乘以比例。反过来，先把画布坐标除以比例，再加上相机偏移，就能找到光标指向的地图位置。</p>

<p lang="en">On a Canvas map, a marker should stay under the cursor when you point at it and zoom. Seed Map’s example stores the camera offset in world coordinates and keeps scale separately. To draw a world point, subtract the camera offset and multiply by scale. To find the map point under the cursor, divide the canvas coordinates by scale and add the camera offset.</p>

<p lang="zh-CN">在使用同一坐标系的 Canvas 2D 绘制循环中，把光标位置换算成与绘制变换一致的画布坐标，再将它和新的正比例传给代码块里的函数。函数使用旧比例求出锚点，再计算新相机偏移。更新后重绘。这个例子是对作者坐标变换的推导，覆盖缩放的坐标计算。</p>

<p lang="en">In a Canvas 2D drawing loop using this coordinate model, convert the cursor position to the same canvas coordinates used by the drawing transform. Pass that position and a new positive scale to the function, then redraw. The function finds the anchor using the old scale and calculates the new camera offset. The example derives the zoom calculation from the author’s coordinate transforms.</p>

<p lang="zh-CN">可用一个简单的数值检查验证结果。相机横坐标为 10、比例为 1 时，画布横坐标 100 对应世界横坐标 110。以该处为锚点把比例改为 2，相机横坐标应变为 60，世界横坐标 110 仍投影到 100。如果实际界面里的标记发生漂移，先核对指针位置与绘制变换使用的坐标原点和单位。</p>

<p lang="en">Use a small numerical check. With the camera’s x position at 10 and scale at 1, canvas x = 100 maps to world x = 110. Zoom to scale 2 around that point and the camera’s x position should become 60, leaving world x = 110 projected to canvas x = 100. If a marker drifts in the interface, check that pointer coordinates and the drawing transform use the same origin and units.</p>
