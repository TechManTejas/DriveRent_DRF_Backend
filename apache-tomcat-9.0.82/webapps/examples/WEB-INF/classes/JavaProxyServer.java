import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Enumeration;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class JavaProxyServer extends HttpServlet {
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String authorizationHeader = request.getHeader("Authorization");
        String requestURI = request.getRequestURI();

        if (authorizationHeader == null || "/auth".equals(requestURI)) {
            String djangoServerUrl = "http://localhost:8000"; // URL of your Django server
            String proxyUrl = djangoServerUrl + requestURI;

            URL url = new URL(proxyUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod(request.getMethod());

            // Copy request headers from the original request
            Enumeration<String> headerNames = request.getHeaderNames();
            while (headerNames.hasMoreElements()) {
                String headerName = headerNames.nextElement();
                String headerValue = request.getHeader(headerName);
                connection.setRequestProperty(headerName, headerValue);
            }

            // Forward request to Django server
            int responseCode = connection.getResponseCode();
            response.setStatus(responseCode);

            // Copy response headers from the Django response
            Map<String, List<String>> headerFields = connection.getHeaderFields();
            for (Map.Entry<String, List<String>> entry : headerFields.entrySet()) {
                if (entry.getKey() != null) {
                    for (String value : entry.getValue()) {
                        response.addHeader(entry.getKey(), value);
                    }
                }
            }

            // Copy response body from the Django response
            try (InputStream is = connection.getInputStream();
                    OutputStream os = response.getOutputStream()) {
                byte[] buffer = new byte[4096];
                int bytesRead;
                while ((bytesRead = is.read(buffer)) != -1) {
                    os.write(buffer, 0, bytesRead);
                }
            }
        }
    }
}
