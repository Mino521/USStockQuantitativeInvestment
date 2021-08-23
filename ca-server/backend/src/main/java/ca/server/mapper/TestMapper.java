package ca.server.mapper;

import ca.server.entity.ArchiveContent;
import org.apache.ibatis.annotations.Mapper;


import java.util.List;

@Mapper
public interface TestMapper {
    List<ArchiveContent> getAll();
}
