from flask_navigation import Navigation

navigation = Navigation()#导航栏自定义部分

navigation.Bar('top', [
    navigation.Item('首页', 'auth.login'),
    navigation.Item('分类', 'auth.login'),
    navigation.Item('工具', 'auth.login',items=[
      navigation.Item('1','auth.login'),
    ])
])