# Tutorial: Creating a Robot from a Template (4-Axis SCARA)

In the previous example, we took the time to build a 2-bar robot project from scratch. This time, we will explore how to start with a pre-configured template. 

Currently, templates are available for 2-axis, 4-axis, 6-axis, and 7-axis robots. In this chapter, we will create a 4-axis SCARA robot using its respective template.

---

## Step 1: Create a New Robot

First, navigate to the **Home** screen and click the **Create New Robot** button.

<figure markdown="span">
    ![create_robot_highlighted](images/create_new_robot_highlight.png){ width="1000" }
    <figcaption>Click the <strong>Create New Robot</strong> button on the Home screen</figcaption>
</figure>

---

## Step 2: Select the Template

1. In the creation menu, select **Robot Template**.
2. Choose the **4-Axis SCARA** option from the list.
3. Enter your desired robot name.
4. Click **Create**.

<figure markdown="span">
    ![select_template](images/select_scara_template.png){ width="1000" }
    <figcaption>Select <strong>Robot Template</strong>, choose the 4-Axis SCARA, and click Create</figcaption>
</figure>

---

## Step 3: Virtual Verification

Once the robot is created, you will be directed to the main setup screen.

<figure markdown="span">
    ![setup_screen](images/setup_screen_scara.png){ width="1000" }
    <figcaption>Main Setup Screen for the SCARA Robot</figcaption>
</figure>

Since the template pre-fills the structural and dynamic configurations, you can bypass those steps and test the robot immediately:
1. Navigate directly to the **Virtual Verification** tab.
2. Click **Activate Simulation**.

---

## Conclusion

You have successfully set up a SCARA robot using a provided template! 

Since physical servo motors are likely not connected or prepared at this stage, you can test your setup in a simulated environment. The tutorial for integrating and communicating with Isaac Sim (via the Stellar Bridge extension) is covered in detail here: [Link to Isaac Sim Integration Tutorial](#)




<!-- 앞선 예제에서는 2bar 로봇 프로젝트를 직접 작성해보는 시간을 가졌었다.
이번엔 이미 작성되어있는 탬플릿으로부터 시작해보고자한다.

현재 2축, 4축, 6축, 7축의 예제가 있다.

이번 챕터에서는 4축 스카라 로봇을 탬플릿을 이용해 생성하여보자.

먼저 다음과 같이 홈화면에서 Create New Robot을 클릭한다. 

<create new robot 네모친 그림>
<robot templete 네모치고 4축 스카라 선택한 그림>
위와같이 클릭한다음, 원하는 로봇이름을 작성하고 Create 버튼을 누른다.

<setup화면으로 이동한 그림..>
바로 virtual verification 으로 이동하여 Activate Simulation을 누른다.

이렇게 템플릿으로 스카라 로봇을 세팅하여 보았다.

현재 실제 서보가 준비되어있지 않을것이므로, isaacsim과 연동하는 예제는 여기서(링크) 다룬다.  -->
