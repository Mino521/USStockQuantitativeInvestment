package ca.server.controller;

import ca.server.DTO.ArchiveContentDTO;
import ca.server.DTO.ArchiveFilterDTO;
import ca.server.entity.ArchiveContent;
import ca.server.mapper.DataMapper;
import ca.server.mapper.ResultMapper;
import ca.server.service.DataService;
import ca.server.service.TestService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import springfox.documentation.swagger2.mappers.RequestParameterMapper;

import java.math.BigDecimal;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/database")
@Api(tags = "database",value = "get and update data from database")
public class DataController {
    @Autowired
    private TestService testService;

    @Autowired
    private DataService dataService;

    @Deprecated
    @PostMapping("/abc")
    public String abc(){
        return "hello";
    }

    @Deprecated
    @GetMapping("/getall")
    @ResponseBody
    public List<ArchiveContent> getAll(){
        return testService.getAll();
    }

    @Deprecated
    @GetMapping("/getallarchive")
    @ResponseBody
    public ResultMapper<List<ArchiveContent>> getAllArchiveContent() throws SQLException, ClassNotFoundException, SQLException {
        List<ArchiveContent> res = testService.getAll();
        if(res == null){
            return ResultMapper.errorResultMapper("No data found.");
        }
        return ResultMapper.successResultMapper(res);
    }

    @GetMapping("/getArchiveByFilter")
    @ApiOperation(value = "get data by given filter")
    /*
    @ApiImplicitParams({
            @ApiImplicitParam(name = "cik",dataType = "List",example = "[1800,...]",required = false),
            @ApiImplicitParam(name = "ticket", dataType = "String",example = "LEGX",required = false),
            @ApiImplicitParam(name = "yearStart",dataType = "Integer",example = "2020",required = false),
            @ApiImplicitParam(name = "yearEnd",dataType = "Integer",example = "2020",required = false),
            @ApiImplicitParam(name = "Stata", dataType = "String",example = "FL",required = false),
            @ApiImplicitParam(name = "office", dataType = "String",example = "Office of Life Sciences",required = false),
            @ApiImplicitParam(name = "pageSize",dataType = "Integer",example = "10",required = false),
            @ApiImplicitParam(name = "pageIndex",dataType = "Integer",example = "1",required = false)
    })
     */
    @ResponseBody
    public List<ArchiveContentDTO> getArchiveByFilter(ArchiveFilterDTO archiveFilterDTO){
        if(archiveFilterDTO.getPageSize()!=null&&archiveFilterDTO.getPageIndex()!=null) {
            archiveFilterDTO.setPageIndex(archiveFilterDTO.getPageIndex() * archiveFilterDTO.getPageSize());
        }
        return dataService.getArchiveByFilter(archiveFilterDTO);
    }
    @ApiOperation(value = "update data by id and column name")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "id",value = "the record key",required = true),
            @ApiImplicitParam(name = "columnName",value = "the column name you want to update",required = true),
            @ApiImplicitParam(name = "columnValue", value = "correct value",required = true,example = "123")
    })
    @PostMapping("/updateArchiveData")
    public ResponseEntity<?> updateArchiveData(Integer id, String columnName, BigDecimal columnValue){
        Long affectColumn = dataService.updateArchiveData(id, columnName, columnValue);
        if (affectColumn>0) {
            return new ResponseEntity<>("" + affectColumn + " affected column(s)", HttpStatus.OK);
        }
        return new ResponseEntity<>("error",HttpStatus.BAD_REQUEST);
    }

}
