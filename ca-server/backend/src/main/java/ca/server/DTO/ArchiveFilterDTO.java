package ca.server.DTO;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;
@Data
public class ArchiveFilterDTO {

    private List<Integer> cik;
    private String ticket;
    private Integer yearStart;
    private Integer yearEnd;
    private String state;
    private String office;
    private Integer pageSize;
    private Integer pageIndex;
}
