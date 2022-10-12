package com.frankly.restapi.service;

import com.frankly.restapi.domain.PropertyChangeDTO;
import com.frankly.restapi.domain.PropertyDTO;
import com.frankly.restapi.mapper.PropertyMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class PropertyService implements PropertyServiceInterface {

    private final PropertyMapper propertyMapper;

    @Override
    public void createProperty(PropertyDTO propertyDTO) throws Exception {
        propertyMapper.createProperty(propertyDTO);
    }

    @Override
    public List<PropertyDTO>readProperty(int politicianID) throws Exception {
        return propertyMapper.readProperty(politicianID);
    }
    @Override
    public List<PropertyChangeDTO>readPropertyChange(int politicianID) throws Exception {
        return propertyMapper.readPropertyChange(politicianID);
    }

    @Override
    public void updateProperty(PropertyDTO propertyDTO) throws Exception {
        propertyMapper.updateProperty(propertyDTO);
    }

    @Override
    public void deleteProperty(PropertyDTO propertyDTO)throws Exception {
        propertyMapper.deleteProperty(propertyDTO);
    }

}
