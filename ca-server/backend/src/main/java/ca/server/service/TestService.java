package ca.server.service;

import ca.server.entity.ArchiveContent;
import ca.server.mapper.TestMapper;
import org.springframework.stereotype.Service;
import javax.annotation.Resource;
import java.util.List;

@Service
public class TestService {
    @Resource
    private TestMapper testMapper;

    public List<ArchiveContent> getAll(){
        return testMapper.getAll();
    }

}
