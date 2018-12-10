import java.io.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;
import java.util.Map;

/**
 * Created by Dqd on 2018/12/8.
 */

public class Main {
    public static void insertdata(List<School> list){
        try {
            Class.forName("com.mysql.jdbc.Driver");//加载数据库驱动
            System.out.println("加载数据库驱动成功");
            String url="jdbc:mysql://localhost:3306/gaokao?useUnicode=true&characterEncoding=utf-8";//声明数据库test的url
            String user="root";//数据库的用户名
            String password="";//数据库的密码
            //建立数据库连接，获得连接对象conn(抛出异常即可)
            Connection conn= DriverManager.getConnection(url, user, password);
            System.out.println("连接数据库成功");
            //生成一条mysql语句
            String sql="";
            Statement stmt=conn.createStatement();//创建一个Statement对象
            for(School s : list){
                Integer tmp = null;
                if(!s.getNum().equals("--")){
                    tmp = Integer.valueOf(s.getNum());
                }
                //"insert into users(username,password,age,sex) values('小别','123456',22,0)";
                sql = "insert into school(schoolid,schoolname,province,schooltype,schoolproperty,f985,f211,s_level,membership,schoolnature,shoufei,jianjie,schoolcode,ranking,rankingCollegetype,guanwang,oldname,num)"+
                        " values("+s.getSchoolid()+",'"+s.getSchoolname()+"','"+s.getProvince()+"','"+s.getSchooltype()+"','"+s.getSchoolproperty()+"',"+Integer.valueOf(s.getF985())+","+Integer.valueOf(s.getF211())+",'"+s.getLevel()+"','"+s.getMembership()+"','"+s.getSchoolnature()+"','"+s.getShoufei()+"','"+s.getJianjie()+"','"+s.getSchoolcode()+"',"+Integer.valueOf(s.getRanking())+","+Integer.valueOf(s.getRankingCollegetype())+",'"+s.getGuanwang()+"','"+s.getOldname()+"',"+tmp+")";
                System.out.println("sql-->"+sql);
                stmt.executeUpdate(sql);//执行sql语句
                System.out.println("插入到数据库成功");
            }
            conn.close();
            System.out.println("关闭数据库成功");
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }//
        catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
     public static void main(String[] args)throws Exception{
         File f = new File("F:/gaokao-master/gaokao/spiders/school11.json");
         FileInputStream fis = new FileInputStream(f);
         InputStreamReader isr = new InputStreamReader(fis);
         BufferedReader bf = new BufferedReader(isr);
         String tmp="";
         StringBuffer sb = new StringBuffer();
         while((tmp = bf.readLine())!=null){
             sb.append(tmp.trim());
         }
         //School ob = JsonUtils.jsonToPojo(tmp11,School.class);
         List<School> list = JsonUtils.jsonToList(sb.toString(),School.class);
         for (School ob : list) {
            System.out.println(ob);
         }
         //System.out.println(ob.getFirstrateclass());
         insertdata(list);

    }
}
