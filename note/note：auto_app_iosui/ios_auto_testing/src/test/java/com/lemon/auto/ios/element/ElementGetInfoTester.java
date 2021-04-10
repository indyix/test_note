package com.lemon.auto.ios.element;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.Rectangle;
import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.internal.Yaml;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class ElementGetInfoTester {
	/**
	 * mac osx：10.14 appium：v.12.1 xcode：10.1 iOS:12.1
	 * 
	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "12.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/happy/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置app设置
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);

		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		
		IOSElement element = driver.findElementByAccessibilityId("Action Sheets");

//		4
//		getText
//		返回元素的可见文本
		System.out.println(element.getText());//Action Sheets
		
//		5
//		getTagName
//		返回元素标签名，如XCUIElementTypeCell
		System.out.println(element.getTagName());//XCUIElementTypeStaticText
		
//		6
//		getAttribute
//		返回元素相关属性，支持属性如下：
//		UID,accessibilityContainer,accessible,enabled,frame,label,name,rect,type,value,visible,wdAccessibilityContainer,wdAccessible,wdEnabled,wdFrame,wdLabel,wdName,wdRect,wdType,wdUID,wdValue,wdVisible
		System.out.println(element.getAttribute("enabled"));//true
		
//		7
//		isDisplayed
//		确定当前是否显示了元素
		System.out.println(element.isDisplayed());//true
		
//		8
//		isEnabled
//		确定当前是否启用了某个元素
		System.out.println(element.isEnabled());//true
		
//		9
//		isSelected
//		确定是否选中了表单或类似表单的元素(复选框、select等)
//		System.out.println(element.isSelected()); //
		
//		10
//		getId
//		获取元素的ID（十六进制哈希字符串）
		System.out.println(element.getId());//27000000-0000-0000-4A21-000000000000
		
//		11
//		getSize
//		确定元素的大小(以像素为单位)，大小将作为具有宽度和高度属性的对象返回
		Dimension dimension = element.getSize();
		System.out.println(dimension.getWidth()+","+dimension.getHeight());//119,24
		
//		12
//		getLocation
//		确定元素在页面或屏幕上的位置，点(0,0)指向页面的左上角。元素的坐标以带有x和y属性的JSON对象返回
		Point point = element.getLocation();
		System.out.println(point.getX()+","+point.getY());//18,82
		
//		13
//		getRect
//		获取元素的维数和坐标
		Rectangle rectangle = element.getRect();
		System.out.println(rectangle.x);
		System.out.println(rectangle.y);
		System.out.println(rectangle.getWidth());
		System.out.println(rectangle.getHeight());

//		Thread.sleep(3000);
//		driver.quit();
	}

}
