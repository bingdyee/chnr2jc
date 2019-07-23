package com.forhome.zhijia.checkoutlog.pojo.po;

import com.baomidou.mybatisplus.annotations.TableField;
import com.baomidou.mybatisplus.annotations.TableName;
import com.forhome.zhijia.common.base.BaseEntity;

/**
 * 
 *
 * @author devuser 
 * @date 2019-07-23
 */
@TableName("l_check_out_log")
public class CheckOutLog extends BaseEntity {

    /**日志ID */
    @TableField("id")
    private Long id;
    /**序号 */
    @TableField("sort")
    private Integer sort;
    /**状态，0-删除；1-正常；2-禁用；3-历史 */
    @TableField("status")
    private Integer status;
    /**uuid */
    @TableField("uuid")
    private String uuid;
    /**创建时间 */
    @TableField("create_date")
    private String createDate;
    /**修改时间 */
    @TableField("update_date")
    private String updateDate;
    /**创建人uuid */
    @TableField("creater_user_uuid")
    private String createrUserUuid;
    /**修改人uuid */
    @TableField("updater_user_uuid")
    private String updaterUserUuid;
    /**记录类型，0-退房 */
    @TableField("type")
    private Integer type;
    /**学号 */
    @TableField("student_num")
    private String studentNum;
    /**学生姓名 */
    @TableField("user_name")
    private String userName;
    /**用户UUID */
    @TableField("user_uuid")
    private String userUuid;
    /**宿舍楼UUID */
    @TableField("dorm_uuid")
    private String dormUuid;
    /**宿舍楼名称 */
    @TableField("dorm_name")
    private String dormName;
    /**宿舍房间UUID */
    @TableField("dorm_room_uuid")
    private String dormRoomUuid;
    /**宿舍房间号 */
    @TableField("dorm_room_name")
    private String dormRoomName;
    /**床号 */
    @TableField("bed_num")
    private Integer bedNum;
    /**床位UUID */
    @TableField("bed_uuid")
    private String bedUuid;
    /**学校的objectid */
    @TableField("objectid")
    private String objectid;
    /**学校名称 */
    @TableField("school_name")
    private String schoolName;
    /**入住时间 */
    @TableField("check_out_date")
    private String checkOutDate;
    /**备注 */
    @TableField("remark")
    private String remark;
    /**备用字段1 */
    @TableField("temp_1")
    private String temp1;
    /**备用字段2 */
    @TableField("temp_2")
    private String temp2;
    /**备用字段3 */
    @TableField("temp_3")
    private String temp3;

    public CheckOutLog() {
		super();
	}

    public void setId(Long id) {
        this.id = id;
    }

    public Long getId() {
        return this.id;
    }

    public void setSort(Integer sort) {
        this.sort = sort;
    }

    public Integer getSort() {
        return this.sort;
    }

    public void setStatus(Integer status) {
        this.status = status;
    }

    public Integer getStatus() {
        return this.status;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public String getUuid() {
        return this.uuid;
    }

    public void setCreateDate(String createDate) {
        this.createDate = createDate;
    }

    public String getCreateDate() {
        return this.createDate;
    }

    public void setUpdateDate(String updateDate) {
        this.updateDate = updateDate;
    }

    public String getUpdateDate() {
        return this.updateDate;
    }

    public void setCreaterUserUuid(String createrUserUuid) {
        this.createrUserUuid = createrUserUuid;
    }

    public String getCreaterUserUuid() {
        return this.createrUserUuid;
    }

    public void setUpdaterUserUuid(String updaterUserUuid) {
        this.updaterUserUuid = updaterUserUuid;
    }

    public String getUpdaterUserUuid() {
        return this.updaterUserUuid;
    }

    public void setType(Integer type) {
        this.type = type;
    }

    public Integer getType() {
        return this.type;
    }

    public void setStudentNum(String studentNum) {
        this.studentNum = studentNum;
    }

    public String getStudentNum() {
        return this.studentNum;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getUserName() {
        return this.userName;
    }

    public void setUserUuid(String userUuid) {
        this.userUuid = userUuid;
    }

    public String getUserUuid() {
        return this.userUuid;
    }

    public void setDormUuid(String dormUuid) {
        this.dormUuid = dormUuid;
    }

    public String getDormUuid() {
        return this.dormUuid;
    }

    public void setDormName(String dormName) {
        this.dormName = dormName;
    }

    public String getDormName() {
        return this.dormName;
    }

    public void setDormRoomUuid(String dormRoomUuid) {
        this.dormRoomUuid = dormRoomUuid;
    }

    public String getDormRoomUuid() {
        return this.dormRoomUuid;
    }

    public void setDormRoomName(String dormRoomName) {
        this.dormRoomName = dormRoomName;
    }

    public String getDormRoomName() {
        return this.dormRoomName;
    }

    public void setBedNum(Integer bedNum) {
        this.bedNum = bedNum;
    }

    public Integer getBedNum() {
        return this.bedNum;
    }

    public void setBedUuid(String bedUuid) {
        this.bedUuid = bedUuid;
    }

    public String getBedUuid() {
        return this.bedUuid;
    }

    public void setObjectid(String objectid) {
        this.objectid = objectid;
    }

    public String getObjectid() {
        return this.objectid;
    }

    public void setSchoolName(String schoolName) {
        this.schoolName = schoolName;
    }

    public String getSchoolName() {
        return this.schoolName;
    }

    public void setCheckOutDate(String checkOutDate) {
        this.checkOutDate = checkOutDate;
    }

    public String getCheckOutDate() {
        return this.checkOutDate;
    }

    public void setRemark(String remark) {
        this.remark = remark;
    }

    public String getRemark() {
        return this.remark;
    }

    public void setTemp1(String temp1) {
        this.temp1 = temp1;
    }

    public String getTemp1() {
        return this.temp1;
    }

    public void setTemp2(String temp2) {
        this.temp2 = temp2;
    }

    public String getTemp2() {
        return this.temp2;
    }

    public void setTemp3(String temp3) {
        this.temp3 = temp3;
    }

    public String getTemp3() {
        return this.temp3;
    }


}