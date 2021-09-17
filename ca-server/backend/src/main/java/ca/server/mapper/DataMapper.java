package ca.server.mapper;

import ca.server.DTO.ArchiveContentDTO;
import ca.server.DTO.ArchiveFilterDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

@Mapper
public interface DataMapper {

    public List<ArchiveContentDTO> getArchiveByFilter(@Param("DTO") ArchiveFilterDTO archiveFilterDTO);

    public Long updateArchiveData(@Param(value = "id")Integer id,
                                  @Param(value = "columnName")String columnName,
                                  @Param(value = "columnValue") BigDecimal columnValue);

    public int getArchiveCountByFilter(@Param("DTO") ArchiveFilterDTO archiveFilterDTO);
}
