package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.time.Duration;
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

import io.appium.java_client.appmanagement.ApplicationState;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class Gestures_07_DragFromToForDuration_Tester {
	/**
	 * 命令
		mobile: dragFromToForDuration
		备注
		通过坐标点执行拖放手势。可以在控件上执行，也可以在屏幕上执行
		参数
		element 
		控件ID（作为十六进制哈希字符串）。 如果设置了element参数，则x、y代表的是以当前element为边界的xy轴。若未设置，则x,y代表的是以手机屏幕为边界
		duration 
		浮点数范围[0.5,60]。表示开始拖动点之前的点击手势需要多长时间才能开始拖动。
		必需参数
		fromX
		起始拖动点的x坐标（类型float）。必需参数
		
		fromY
		起始拖动点的y坐标（类型float）。必需参数
		
		toX
		结束拖曳点的x坐标（类型float）。必需参数
		
		toY
		结束拖动点的y坐标（类型float）。必需参数
		示例
		// Java 
		JavascriptExecutor js = (JavascriptExecutor) driver; 
		Map<String, Object> params = new HashMap<>(); 
		params.put("duration", 1.0); 
		params.put("fromX", 100); 
		params.put("fromY", 100); 
		params.put("toX", 200); 
		params.put("toY", 200); 
		params.put("element", ((RemoteWebElement) element).getId()); 
		js.executeScript("mobile: dragFromToForDuration", params); 
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

		Thread.sleep(2000);
		Map<String, Object> params= new HashMap<String, Object>();
		params.put("duration", 0.5);
		params.put("fromX", 155.0);
		params.put("fromY", 400.0);
		params.put("toX", 155.0);
		params.put("toY", 300.0);
		driver.executeScript("mobile: dragFromToForDuration", params);

//		Thread.sleep(3000);
//		driver.quit();

	}

}
