import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.io.IOException;

/**
 * 文件上传
 * 使用注解@MultipartConfig将一个Servlet标注为支持文件上传
 * Servlet将multipart/form-data的POST请求封装成Part，通过Part对上传文件进行操作
 */
@WebServlet("/uploadServlet")
@MultipartConfig//如果是文件上传，必须要加！
public class UploadServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("文件上传。。。");
        //设置请求编码
        request.setCharacterEncoding("UTF-8");
        //获取普通表单项（获取参数）
        String information = request.getParameter("information");//表单中表单元素的name属性值
        System.out.println("information:" + information);

        //获取Part对象（Servlet将multipart/form-data的POST请求封装成Part，通过Part对上传文件进行操作）
        Part part = request.getPart("myFile");//表单中文件域的name属性值
        //通过Part对象得到上传文件名
        String cd = part.getHeader("Content-Disposition");
        String fileName = cd.substring(cd.lastIndexOf("=")+2,cd.length()-1);
//        String fileName = part.getSubmittedFileName();
        System.out.println("上传文件名：" +fileName);
        //得到文件存放的路径
        String filePath = request.getServletContext().getRealPath("/");
        System.out.println("文件存放的路径："+ filePath);
        //上传文件到指定目录
        part.write(filePath+"/"+fileName);
    }
}

