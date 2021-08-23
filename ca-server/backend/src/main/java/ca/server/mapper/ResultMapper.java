package ca.server.mapper;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class ResultMapper<E> implements java.io.Serializable{

    private static final long serialVersionUID = 5804493567777773963L;

    /**
     * request success or not
     */
    private boolean success;

    /**
     * error code
     */
    private String errorCode;

    /**
     * error info
     */
    private String info;

    /**
     * returned data
     */
    private E data;

    public ResultMapper() {
    }

    public ResultMapper(boolean success) {
        this.success = success;
    }

    public ResultMapper<E> setSuccess(boolean success) {
        this.success = success;
        return this;
    }

    public ResultMapper<E> setErrorCode(String errorCode) {
        this.errorCode = errorCode;
        return this;
    }

    public ResultMapper<E> setInfo(String info) {
        this.info = info;
        return this;
    }

    public ResultMapper<E> setData(E data) {
        this.data = data;
        return this;
    }

    public static <T> ResultMapper<T> successResultMapper() {
        ResultMapper<T> resultMapper = new ResultMapper<>(true);
        return resultMapper;
    }

    public static <T> ResultMapper<T> successResultMapper(T data) {
        ResultMapper<T> resultMapper = new ResultMapper<>(true);
        resultMapper.setData(data);
        return resultMapper;
    }

    public static <T> ResultMapper<T> errorResultMapper(String info) {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setInfo(info);
        return resultMapper;
    }

    public static <T> ResultMapper<T> errorResultMapper(String info, T data) {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setInfo(info);
        resultMapper.setData(data);
        return resultMapper;
    }

    public static <T> ResultMapper<T> errorResultMapper(String errorCode, String info) {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setErrorCode(errorCode);
        resultMapper.setInfo(info);
        return resultMapper;
    }

    public static <T> ResultMapper<T> errorResultMapper(String errorCode, String info, T data) {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setErrorCode(errorCode);
        resultMapper.setInfo(info);
        resultMapper.setData(data);
        return resultMapper;
    }

    /**
     * Error about client parameters
     * @return
     */
    public static <T> ResultMapper<T> errorResultMapper400() {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setInfo("Client Error");
        resultMapper.setErrorCode("400");
        return resultMapper;
    }

    /**
     * Error about client parameters
     * @return
     */
    public static <T> ResultMapper<T> errorResultMapper400(String info) {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setInfo(info);
        resultMapper.setErrorCode("400");
        return resultMapper;
    }

    /**
     * An error occurred inside the server
     * @return
     */
    public static <T> ResultMapper<T> errorResultMapper500() {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setInfo("Server Error");
        resultMapper.setErrorCode("500");
        return resultMapper;
    }

    /**
     * An error occurred inside the server
     * @return
     */
    public static <T> ResultMapper<T> errorResultMapper500(String info) {
        ResultMapper<T> resultMapper = new ResultMapper<>(false);
        resultMapper.setInfo(info);
        resultMapper.setErrorCode("500");
        return resultMapper;
    }

}
