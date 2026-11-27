---
category: "coding"
summaryEn: "Keep development, sales-office, and agent addresses in separate evidence groups. A fixture with addresses in different districts lets you check that each answer cites the right field."
summaryZh: "把楼盘、售楼处和经纪人地址保存在不同的证据组里，再用一条跨区记录检查回答是否引用了正确字段。"
tags: ["rag", "retrieval", "data-modeling"]
titleEn: "Keep sales-office addresses out of property-location answers"
titleZh: "让房产 RAG 用正确的地址回答楼盘位置"
blocks: [{"kind": "notice", "text": {"en": "Field roles can prevent a sales-office address from being used as property evidence. The source still has to supply the correct property address.", "zh": "字段角色可以防止售楼处地址被当作楼盘位置证据。楼盘地址本身仍须由数据源准确提供。"}, "title": {"en": "What field roles can fix", "zh": "字段角色能解决什么"}}]
type: "workflows"
version: "Field projection pattern documented on 2026-11-26"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T10:02:34+08:00"
sources: [{"title": "Nieruchomosci Online RAG in Python: Keep Sales Offices Out of Home Locations", "url": "https://dev.to/vexaloom-labs/nieruchomosci-online-rag-in-python-keep-sales-offices-out-of-home-locations-182h"}]
---
<p lang="zh-CN">同一条房产记录可能同时包含楼盘地址和售楼处地址。vexaloom-labs 的实验笔记用一组构造数据说明了其中的风险。把所有字段值拼成一段文本后，售楼处的行政区可能恰好匹配查询，回答也可能引用这条记录，把楼盘放到错误的位置。</p>

<p lang="en">A property record can contain both a development address and a sales-office address. A lab note from vexaloom-labs illustrates the risk with a constructed fixture. Once all field values are joined into one passage, the sales office’s district can match the query and lead to an answer that cites the record while placing the development in the wrong location.</p>

<h2><span lang="zh-CN">索引前保留地址用途</span><span lang="en">Preserve each address’s role before indexing</span></h2>

<p lang="zh-CN">先确认输入记录是否已经区分楼盘、售楼处和经纪人字段，再按字段清单提取三组证据。楼盘组保留 address、city、district 等位置字段，售楼处组保留 salesOfficeAddress、salesOfficeCity 等联系字段，经纪人地址留在经纪人组。用楼盘组检索房产位置，用联系组回答去哪里咨询。检查输出时，同时核对引用内容和证据的字段角色。</p>

<p lang="en">First check that the input records distinguish development, sales-office, and agent fields. Then project them into three evidence groups. Keep fields such as address, city, and district with the development. Keep salesOfficeAddress and salesOfficeCity with the sales office, and place the agent’s address in the agent group. Search development evidence for property locations and contact evidence for where to make inquiries. When reviewing an answer, check both the cited text and the role of the field it came from.</p>

<p lang="zh-CN">构造一条楼盘与售楼处分属不同区的记录，分别询问楼盘在哪个区和售楼处在哪个区。预期是两次回答各自引用对应字段。如果位置问题引用了售楼处，先检查建索引前的字段提取，再检查检索是否限定了证据角色。这是依据作者笔记设计的回归检查，构造数据只覆盖这个错误场景。</p>

<p lang="en">Create a record with the development and sales office in different districts, then ask for each district separately. Each answer should cite its corresponding field. If the location answer cites the sales office, inspect field extraction before indexing, then check whether retrieval restricts the evidence by role. This regression check follows the author’s note and covers the failure demonstrated by the constructed fixture.</p>
