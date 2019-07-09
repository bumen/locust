## idea中部署debug
 * SDK需要使用python2.7
   + 如果使用3.7导致monkey.patch_all()中thread模块失败
   
 * 引入模块
   + 目录/e/project/github/locust/locust
   + 必需是第2个locust
   
 * 写一个测试入口py
   + 在测试入口中引入locust.main
     > 注意不能直接在main中启动调试。因为main有相对路径引入的模块
   + test_local.py
       ```
        from locust.main import main
        
        
        if __name__ == '__main__':
            main()
        
       ```
   
 * 配置参数
 
 
 * 开始设置