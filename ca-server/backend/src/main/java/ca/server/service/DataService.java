package ca.server.service;

import ca.server.DTO.ArchiveContentDTO;
import ca.server.DTO.ArchiveFilterDTO;
import ca.server.mapper.DataMapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

@Service
public class DataService {
    @Resource
    private DataMapper dataMapper;
    public List<ArchiveContentDTO> getArchiveByFilter(ArchiveFilterDTO archiveFilterDTO){
        return dataMapper.getArchiveByFilter(archiveFilterDTO);

    }
    public Long updateArchiveData(@Param(value = "id")Integer id,
                                     @Param(value = "columnName")String columnName,
                                     @Param(value = "columnValue") BigDecimal columnValue){
        return dataMapper.updateArchiveData(id, columnName, columnValue);
    }
}
