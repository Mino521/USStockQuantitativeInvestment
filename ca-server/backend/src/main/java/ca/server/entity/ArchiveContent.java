package ca.server.entity;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class ArchiveContent {
    private Integer id;

    private Integer cik;

    private Integer year;

    private BigDecimal earningsPerShare;
}