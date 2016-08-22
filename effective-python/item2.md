# 在代码中使用PEP8规范

PEP8 规范是早期Python创始人Guido制定的一套标准，这套标准广泛地应用在Python的标准库和社区开发项目中，因此，被很多人奉为圭臬。实际上，我认为PEP8不是写死的标准，而是一套帮助开发者提升代码可读性的规范。正如PEP8原文所说:

"""A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important."""

展开举一些列子：

* 一行代码长度不应该超过79字符, 方法定义和类定义之间用2个空行隔开。这正是为了提升代码的可读性.
* 命名方式上，类命名最好是CapitalizedWord， 而方法和变量名最好是lowercase_underscore；其实不推荐用一两个摸不着头脑的字母做变量名，比如：cp（因为这种变量名需要二重认知，如果改为content_provider，其实就很清晰）

以上是一些PEP规范中的例子，其实还有一些是增强可读性的例子：

* 判断语句:
    1. 好:   if a is not b
    2. 不好: if not a is b

* 判断是否为空:
    1. 好:   if not somelist / if somelist
    2. 不好: if len(somelist) == 0 / if len(somelist) != 0

* 避免单行判断或者循环语句, 尽量把 if else / while / try...except..else 语句放在不同行，增加视觉可读性
* import的引用顺序，建议做法是把import都集中在文件顶部，其次引用顺序是 标准类库 > 第三方类库 > 自己的模块(这个其实two scoops of django也提到过):
比如 我们项目中的一个文件的引用是这样的:

```python
from commons.response import APIResponse
from commons.utils import SYS_CODE_MAPPING
from commons.constants import Const
from .serializers import (BindUserWechatSerializer,
                          BindByUnionidSerializer,
                          BindByUidSerializer,
                          GuestBindWechatSerializer
                          )
from users.models import User
from sysusers.models import SysUser
from commons.exceptions import UserApiError
from userapi.helpers import format_info_response
from rest_framework.decorators import api_view
import logging
import datetime
```

按照好的引用，应该是:

```python
import logging
import datetime

from rest_framework.decorators import api_view

from commons.response import APIResponse
from commons.utils import SYS_CODE_MAPPING
from commons.constants import Const
from commons.exceptions import UserApiError

from users.models import User
from sysusers.models import SysUser
from userapi.helpers import format_info_response

from .serializers import (BindUserWechatSerializer,
                          BindByUnionidSerializer,
                          BindByUidSerializer,
                          GuestBindWechatSerializer
                          )
```

重新一排布，其实就会清晰很多。


其实有很多工具可以帮助大家检查代码规范，但是因为各自都有各自的配置标准（vim-flake8），导致依然存在代码风格不一致的情况。建议可以使用pylint集成到git或者代码提交中，引入相同的配置，这样可能会有效规范团队的代码可读性。

稍微研究了一下[Pylilnt](http://www.pylint.org/)：
* 直接扫描所有代码，进行静态检查，分为**C**onvention, **W**arning, **E**rror等级别，检查项都可以做配置。比如我看到一个叫做logging-not-lazy的错误，发现我们在打logger的时候是这样做的：

```python
logger.debug('register_wechat_user: %s' % request.POST)
```
实际上这样做不好，应该使用lazy evaluation的形式

```python
logger.debug('register_wechat_user: %s', request.POST)
```

让logger自己组装参数.

* 静态检查可以查到代码中有多少是重复的部分，然后提示是否应该进行重构。

总之，是一个不错的代码风格检查包
# 想法
之后看是否有时间把pylint的检查直接集成到git或者fabric中。



