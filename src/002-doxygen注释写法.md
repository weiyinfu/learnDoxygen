# group
doxygen中的group会生成module板块。  
group有三种写法：
* `\ingroup xxx`把一个类或者一个函数等添加到一个group
* `\addtogroup xxx`，需要使用`@{`和`}@`包括内容。
* `\defgroup <groupIdentifier> <groupDescription>`，需要使用`@{`和`}@`包括内容。

# 使用section实现中英文
用doxygen生成中英文帮助，主要是通过enabled_sections选项进行控制

```plain
/**
\if english
    This is English.
\else
    汉语注释
\endif
*/
class Example{
    undefined
};
```


if的命令和C语言中预处理命令相似。当english被定义的使用"This is English."注释，
否则默认使用"汉语注释"。
if的条件可以在配置文件中修改（默认为Doxyfile文件）。假如我们现要生成
english帮助，添加以下配置：
ENABLED_SECTIONS       = english

关于ENABLED_SECTIONS的细节可以参考doxygen的说明文档。下面生成就可以得到
英文帮助文档了。如果不定义english，则默认为中文帮助文档。


# 支持的命令
* @file	档案的批注说明。
* @author	作者的信息
* @brief	用于class 或function的简易说明eg：@brief 本函数负责打印错误信息串
* @param	主要用于函数说明中，后面接参数的名字，然后再接关于该参数的说明
* @return	描述该函数的返回值情况eg:@return 本函数返回执行结果，若成功则返回TRUE，否则返回FLASE
* @retval	描述返回值类型，eg:@retval NULL 空字符串。
* @note	注解
* @attention	注意
* @warning	警告信息
* @enum	引用了某个枚举，Doxygen会在该枚举处产生一个链接，eg：@enum CTest::MyEnum
* @var	引用了某个变量，Doxygen会在该枚举处产生一个链接，eg：@var CTest::m_FileKey
* @class	引用某个类，格式：@class <name> [<header-file>] [<header-name> ]，eg:@class CTest "inc/class.h"
* @exception	可能产生的异常描述,eg:@exception 本函数执行可能会产生超出范围的异常
* @file
* @brief One could use the `\brief` command with one of the above comment blocks. This command ends at the end of a paragraph, so the detailed description follows after an empty line.
```plain
/*! @brief Brief description.
*         Brief description continued.
* 
* Detailed description starts here.
   */
```
* @param 用于描述函数的入参
* @return 用于描述函数的返回值

# 注释实例
```plain
/**
  * @file             sensor.c
  * @author           JonesLee
  * @email           Jones_Lee3@163.com
  * @version        V4.01
  * @date            07-DEC-2017
  * @license          GNU General Public License (GPL)  
  * @brief           Universal Synchronous/Asynchronous Receiver/Transmitter 
  * @detail                detail
  * @attention
  *  This file is part of OST.                                                  \n                                                                  
  *  This program is free software; you can redistribute it and/or modify                 \n     
  *  it under the terms of the GNU General Public License version 3 as                     \n   
  *  published by the Free Software Foundation.                                       \n 
  *  You should have received a copy of the GNU General Public License                   \n      
  *  along with OST. If not, see <http://www.gnu.org/licenses/>.                               \n  
  *  Unless required by applicable law or agreed to in writing, software               \n
  *  distributed under the License is distributed on an "AS IS" BASIS,                 \n
  *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.          \n
  *  See the License for the specific language governing permissions and             \n  
  *  limitations under the License.                                                                                           \n
  *                                                                                                                                                           \n
  * @htmlonly 
  * <span style="font-weight: bold">History</span> 
  * @endhtmlonly 
  * Version|Auther|Date|Describe
  * ------|----|------|-------- 
  * V3.3|Jones Lee|07-DEC-2017|Create File
  * <h2><center>&copy;COPYRIGHT 2017 WELLCASA All Rights Reserved.</center></h2>
  */  
```

## 类注释
```plain
/**
* @class <class‐name> [header‐file] [<header‐name]
* @brief brief description
* @author <list of authors>
* @note
* detailed description
*/
```

## 类的成员注释
```plain
class Test
{
public:
    /** @brief A enum, with inline docs */
    enum TEnum 
    {
        TVal1, /**< enum value TVal1. */ 
        TVal2, /**< enum value TVal2. */ 
        TVal3 /**< enum value TVal3. */ 
    } 
   *enumPtr, /**< enum pointer. */
    enumVar; /**< enum variable. */
    /** @brief A constructor. */ 
Test(); 
/** @brief A destructor. */ 
~Test();
 /** @brief a normal member taking two arguments and returning an integer value. */ 
    int testMe(int a,const char *s); 

    /** @brief A pure virtual member. 
    * @param[in] c1 the first argument. 
    * @param[in] c2 the second argument. 
    * @see testMe() 
```

## 函数注释
```plain
        /**
                * @brief                can send the message
                * @param[in]        canx : The Number of CAN
                * @param[in]        id : the can id        
                * @param[in]        p : the data will be sent
                * @param[in]        size : the data size
                * @param[in]        is_check_send_time : is need check out the time out
                * @note        Notice that the size of the size is smaller than the size of the buffer.                
                * @return                
                *        +1 Send successfully \n
                *        -1 input parameter error \n
                *        -2 canx initialize error \n
                *        -3 canx time out error \n
                * @par Sample
                * @code
                *        u8 p[8] = {0};
                *        res_ res = 0; 
                *         res = can_send_msg(CAN1,1,p,0x11,8,1);
                * @endcode
                */                                                        
        extern s32 can_send_msg(const CAN_TypeDef * canx,
                                                        const u32 id,
                                                        const u8 *p,
                                                        const u8 size,
                                                        const u8 is_check_send_time);        

```

## 模块注释
```plain
/**
  * @file             led.h
  * @author           JonesLee
  * @email           Jones_Lee3@163.com
  * @version        V4.01
  * @date            07-DEC-2017
  * @license          GNU General Public License (GPL)  
  * @brief           Controller Area Network
  * @detail                detail
  * @attention
  *  This file is part of OST.                                                  \n                                                                  
  *  This program is free software; you can redistribute it and/or modify                 \n     
  *  it under the terms of the GNU General Public License version 3 as                     \n   
  *  published by the Free Software Foundation.                                       \n 
  *  You should have received a copy of the GNU General Public License                   \n      
  *  along with OST. If not, see <http://www.gnu.org/licenses/>.                               \n  
  *  Unless required by applicable law or agreed to in writing, software               \n
  *  distributed under the License is distributed on an "AS IS" BASIS,                 \n
  *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.          \n
  *  See the License for the specific language governing permissions and             \n  
  *  limitations under the License.                                                                                           \n
  *                                                                                                                                                           \n
  * @htmlonly 
  * <span style="font-weight: bold">History</span> 
  * @endhtmlonly 
  * Version|Auther|Date|Describe
  * ------|----|------|-------- 
  * V3.3|Jones Lee|07-DEC-2017|Create File
  * <h2><center>&copy;COPYRIGHT 2017 WELLCASA All Rights Reserved.</center></h2>
  */  
/** @addtogroup  BSP
  * @{
  */
/**
  * @brief Light Emitting Diode
  */
/** @addtogroup LED 
  * @{
  */ 
#ifndef __LED_H__
#define __LED_H__
#ifdef __cplusplus
extern "C" {
#endif 
        #include "bsp.h"
        extern s32  led_init(Led_TypeDef led);
        extern s32         led_config(void);
        extern s32  led_on(Led_TypeDef led);
        extern s32  led_off(Led_TypeDef led);
        extern s32  led_toggle(Led_TypeDef led);
#ifdef __cplusplus
}
#endif
#endif  /*__LED_H__ */
/**
  * @}
  */
/**
  * @}
  */
/******************* (C)COPYRIGHT 2017 WELLCASA All Rights Reserved. *****END OF FILE****/
```

## 使用include命令把多个文件放在一起
```plain
/*************************************//**
 * @example "My tutorial"
 * 
 * Some context...
 *  @include Source1.cpp
 *
 * More context...
 *  @include Source2.cpp
 ****************************************/
```


# 为group添加详细描述
```plain

/** @defgroup template_api Template API
 *
 *  This is the API for a
 *  <a href="https://www.djangoproject.com/">Django</a>
 *  compatible template system written in C++.
 *  It is somewhat inspired by Stephen Kelly's
 *  <a href="http://www.gitorious.org/grantlee/pages/Home">Grantlee</a>.
 *
 *  A template is simply a text file.
 *  A template contains \b variables, which get replaced with values when the
 *  template is evaluated, and \b tags, which control the logic of the template.
 *
 *  Variables look like this: `{{ variable }}`
 *  When the template engine encounters a variable, it evaluates that variable and
 *  replaces it with the result. Variable names consist of any combination of
 *  alphanumeric characters and the underscore ("_").
 *  Use a dot (.) to access attributes of a structured variable.
 *
 *  One can modify variables for display by using \b filters, for example:
 *  `{{ value|default:"nothing" }}`
 *
 *  Tags look like this: `{% tag %}`. Tags are more complex than variables:
 *  Some create text in the output, some control flow by performing loops or logic,
 *  and some load external information into the template to be used by later variables.
 *
 *  To comment-out part of a line in a template, use the comment syntax:
 *  `{# comment text #}`.
 *
 *  Supported Django tags:
 *  - `for ... empty ... endfor`
 *  - `if ... else ... endif`
 *  - `block ... endblock`
 *  - `extend`
 *  - `include`
 *  - `with ... endwith`
 *  - `spaceless ... endspaceless`
 *  - `cycle`
 *
 *  Extension tags:
 *  - `create` which instantiates a template and writes the result to a file.
 *     The syntax is `{% create 'filename' from 'template' %}`.
 *  - `recursetree`
 *  - `markers`
 *  - `msg` ... `endmsg`
 *  - `set`
 *
 *  Supported Django filters:
 *  - `default`
 *  - `length`
 *  - `add`
 *  - `divisibleby`
 *
 *  Extension filters:
 *  - `stripPath`
 *  - `nowrap`
 *  - `prepend`
 *  - `append`
 *
 *  @{
 */
```

## 在markdown中设置mainpage
```plain
Doxygen Internals {#mainpage}
=================

Introduction
============
```

与之对应，在代码注释里面也可以直接写
```
/*! \mainpage My Personal Index Page
 *
 * \section intro Introduction
 *
 * This is the introduction.
 *
 * \section install Installation
 *
 * \subsection step1 Step 1: Opening the box
 *  
 * etc...
 */
```


# page
除了mainpage，也可以添加一些page，这些配置会放在related部分，与markdown文件地位相当。  
```plain
/*! \page page1 A documentation page
  Leading text.
  \section sec An example section
  This page contains the subsections \ref subsection1 and \ref subsection2.
  For more info see page \ref page2.
  \subsection subsection1 The first subsection
  Text.
  \subsection subsection2 The second subsection
  More text.
*/

/*! \page page2 Another page
  Even more info.
*/
```