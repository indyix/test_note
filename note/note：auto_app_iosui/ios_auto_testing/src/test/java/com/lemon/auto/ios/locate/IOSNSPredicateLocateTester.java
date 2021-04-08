package com.lemon.auto.ios.locate;

import java.net.URL;
import java.util.List;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.MobileBy;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class IOSNSPredicateLocateTester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "13.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/nick/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置APP
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		/**
		 * 1:比较运算符
		 * // 属性 运算符 值
		 *	如：>,<,==,=,>=,<=,!=,<>
		 *	可用于数值和字符串的比较，如name>100 或name == '测试'
		 */
//		String predicateStr = "name = 'id_cell_action_sheet'";
//		driver.findElementByIosNsPredicate(predicateStr).click();
	
//		String predicateStr = "type == 'XCUIElementTypeCell'";
//		String predicateStr = "type = 'XCUIElementTypeCell'";
//		String predicateStr = "type != 'XCUIElementTypeCell'";
//		List<IOSElement> elements = driver.findElements(MobileBy.iOSNsPredicateString(predicateStr));
//		System.out.println(elements.size());
		
		/**
		 * 2:范围运算符
		 * IN,BETWEEN
		 *可用于数值和字符串的范围核对
		 * 如：name BETWEEN {2,10}，name IN {'Tom', 'Jack'}
		*/
//		String predicateStr = "name IN {'id_cell_action_sheet','id_cell_indicators','id_cell_alert66666'}";
//		List<IOSElement> elements = driver.findElements(MobileBy.iOSNsPredicateString(predicateStr));
//		System.out.println(elements.size());
		
		/**
		 * 3:字符串相关运算符
		 * CONTAINS、BEGINSWITH、ENDSWITH
			以字符串“柠檬班软件测试”为例
			包含某个字符串，如：label CONTAINS '软件'
			以某个字符串开头，如：label BEGINSWITH '柠檬'
			以某个字符串结束，如：label ENDSWITH '测试'
			在三个关键字后加上[c]不区分大小写，可用于字母的校验；
			[d]不区分发音符号，即没有重音符号($、#、%等)；
			[cd]即不区分大小写，也不区分发音符号，
			如：name CONTAINS[c] ABcd和name CONTAINS abcd、
			name CONTAINS[c] ABcd 和name CONTAINS ABCD是等同的
			"náive"和"naive”,如果不加关键字d，这两个字符串会认为是不等价的

		 */
		//id_cell_action_sheet
//		String predicateStr = "name CONTAINS 'action'";
//		String predicateStr = "name BEGINSWITH 'id_cell_action'";
//		String predicateStr = "name ENDSWITH 'cell_btn'";
//		List<IOSElement> elements = driver.findElements(MobileBy.iOSNsPredicateString(predicateStr));
//		System.out.println(elements.size());
//		if (elements.size()>0) {
//			elements.get(0).click();
//		}
		
//		String predicateStr = "name CONTAINS[c] 'CELL_BTN'";//cell_btn
//		String predicateStr = "name CONTAINS[c] 'view'";//26
//		String predicateStr = "name CONTAINS 'View'";//21
//		String predicateStr = "name CONTAINS 'view'";//5
//		List<IOSElement> elements = driver.findElements(MobileBy.iOSNsPredicateString(predicateStr));
//		System.out.println(elements.size());
//		if (elements.size()>0) {
//			elements.get(0).click();
//		}
		
		/**
		 * 4：模糊匹配：LIKE
		 * LIKE
			?代表一个字符，*代表多个字符,通配符也接受[cd]
			如：一个元素的label属性为：柠檬班软件测试
			label LIKE '柠檬班软件测试'
			label LIKE '柠檬班?件测试'
			label LIKE '柠檬班??测试'
			label LIKE '柠檬?软?测试'
			label LIKE '*软件测试'
			label LIKE '柠檬班*'
			label LIKE '柠檬*测试'
			label LIKE '柠*软*试'
		 */
		//id_cell_action_sheet
//		String predicateStr1 = "name LIKE 'id_cell_action_sheet'";
//		String predicateStr2 = "name LIKE 'id_cell_?ction_sheet'";
//		String predicateStr3 = "name LIKE 'id_????_action_sheet'";
//		String predicateStr4 = "name LIKE 'id_????_acti??_sheet'";
//		String predicateStr5 = "name LIKE '*_action_sheet'";
//		String predicateStr6 = "name LIKE 'id_cell_*_sheet'";
//		String predicateStr7 = "name LIKE '*_cell_action_*'";
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr1)).size());
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr2)).size());
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr3)).size());
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr4)).size());
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr5)).size());
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr6)).size());
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr7)).size());
		
//		String predicateStr = "name LIKE[c] '*View'";//9
//		String predicateStr = "name LIKE '*View'";//4
//		String predicateStr = "name LIKE '*view'";//4
//		System.out.println(driver.findElements(MobileBy.iOSNsPredicateString(predicateStr)).size());
//		Thread.sleep(3000);
		
		/**
		 * 5：正则表达式：MATCHES
		 */
		//id_cell_action_sheet
		//id_cell_alert
//		String predicateStr = "name MATCHES '^i.+t$'";
//		List<IOSElement> elements = driver.findElements(MobileBy.iOSNsPredicateString(predicateStr));
//		System.out.println(elements.size());
//		if (elements.size()>0) {
//			elements.get(1).click();
//		}
		
		/**
		 * 6:逻辑运算符
		 * AND、&&、OR、||、NOT、 !
		 */
//		String predicateStr = "name = 'id_cell_action_sheet' || name == 'id_cell_alert'";
//		String predicateStr = "name = 'id_cell_action_sheet' OR name == 'id_cell_alert'";
//		String predicateStr = "name = 'id_cell_action_sheet' AND type == 'XCUIElementTypeCell'";
		String predicateStr = "name = 'id_cell_action_sheet' && type == 'XCUIElementTypeCell'";
		List<IOSElement> elements = driver.findElements(MobileBy.iOSNsPredicateString(predicateStr));
		System.out.println(elements.size());
		elements.get(0).click();

		Thread.sleep(3000);
		driver.quit();

	}

}