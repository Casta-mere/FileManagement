# Problem Record

## 12.26

- [ ] 用户问题 

    当某个用户删除之后，仅属于他的文件的权限将如何变更?
    
    在**linux**中，删除某个用户后，该用户之前所拥有的文件的拥有者属性变为unknown，但是uid依然为前拥有者用户的uid。立即创建的一个新用户的uid会继续使用该用户的uid，从而取代该用户获取了该用户之前拥有的文件的所有权。由此可见，Linux可能存在一定的安全风险。

    本项目中的解决方法：


- [ ] 权限问题

    权限用3位2进制数表示(000-111)，通过与001(1)，010(2)，100(4)进行按位与的操作，可以快捷取出对应的权限
     