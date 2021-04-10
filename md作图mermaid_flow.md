画图mermaid

- 编写思路 

```mermaid
graph LR
    id[带文本的矩形]
    -->id4(带文本的圆角矩形)
    -->id3>带文本的不对称的矩形]
    -->id1{带文本的菱形}
    -->id2((带文本的圆形))
    
  st((Start))
	ed((Stop))
  style st fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
  style ed fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 10,5
	
    subgraph one  
    st-->id  
    end
    subgraph two
    id2--yesss-->ed
    end


```

流程图flow

- 编写思路：从前到后一条流的写不要断

```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框

st->op->cond
cond(no)->sub1(right)->op
cond(yes)->io->e
```

```mermaid
graph LR
	st((Start))
	ed((Stop))
  style st fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
  style ed fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 10,5
	
	subgraph 开票后
	wsy(未收银单品流水)
	end
	subgraph 收银后
	ysy>已收银单品流水]
	qkmx>欠款明细]
	dqqk>当前欠款]
	end
	
	kp[开票]
	sy{收银}
	
	st-->kp
	kp-->wsy
	wsy-->sy
	sy-->ysy-->ed
	sy-->qkmx-->ed
	sy-->dqqk-->ed
	
	
	精度-->wsy
	精度-->ysy
	精度-->qkmx
	精度-->dqqk
```

